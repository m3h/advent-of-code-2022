#!/usr/bin/env python3
from dataclasses import dataclass
from collections import defaultdict, namedtuple
import re
import time
import copy
import tqdm
from queue import PriorityQueue
import functools
import ast

import operator

from enum import Enum


class Faces(Enum):
    Up = "U"
    Left = "L"
    Face = "F"
    Right = "R"
    Down = "D"
    Bottom = "B"


class Direction(Enum):
    Up = 0
    Right = 90
    Down = 180
    Left = 270


class Material(Enum):
    Air = "."
    Rock = "#"
    UNSET = "$"


@dataclass
class CubePosition:
    material: Material
    original_x: int
    original_y: int
    original_facing: Direction

    def __repr__(self) -> str:
        return self.material.value


@dataclass
class TurtlePosition:
    face: Faces
    x: int
    y: int
    direction: Direction


class IllformedCubeData(Exception):
    pass


class CubeTurtle:
    def _transition(self, to: Direction):

        p = None
        match self.position.face:
            case Faces.Face:
                match to:
                    case Direction.Up:
                        p = Faces.Up, self.N - 1, self.position.y, Direction.Up
                    case Direction.Right:
                        p = Faces.Right, self.position.x, 0, Direction.Right
                    case Direction.Down:
                        p = Faces.Down, 0, self.position.y, Direction.Down
                    case Direction.Left:
                        p = Faces.Left, self.position.x, self.N - 1, Direction.Left
            case Faces.Up:
                match to:
                    case Direction.Up:
                        p = Faces.Bottom, self.N - 1, self.position.y, Direction.Up
                    case Direction.Right:
                        p = Faces.Right, 0, self.N - self.position.x - 1, Direction.Down
                    case Direction.Down:
                        p = Faces.Face, 0, self.position.y, Direction.Down
                    case Direction.Left:
                        p = Faces.Left, 0, self.position.x, Direction.Down
            case Faces.Left:
                match to:
                    case Direction.Up:
                        p = Faces.Up, self.position.y, 0, Direction.Right
                    case Direction.Right:
                        p = Faces.Face, self.position.x, 0, Direction.Right
                    case Direction.Down:
                        p = Faces.Down, self.N - self.position.y - 1, 0, Direction.Right
                    case Direction.Left:
                        p = (
                            Faces.Bottom,
                            self.N - self.position.x - 1,
                            0,
                            Direction.Right,
                        )
            case Faces.Right:
                match to:
                    case Direction.Up:
                        p = (
                            Faces.Up,
                            self.N - self.position.y - 1,
                            self.N - 1,
                            Direction.Left,
                        )
                    case Direction.Right:
                        p = (
                            Faces.Bottom,
                            self.N - self.position.x - 1,
                            self.N - 1,
                            Direction.Left,
                        )
                    case Direction.Down:
                        p = Faces.Down, self.position.y, self.N - 1, Direction.Left
                    case Direction.Left:
                        p = Faces.Face, self.position.x, self.N - 1, Direction.Left
            case Faces.Down:
                match to:
                    case Direction.Up:
                        p = Faces.Face, self.N - 1, self.position.y, Direction.Up
                    case Direction.Right:
                        p = Faces.Right, self.N - 1, self.position.x, Direction.Up
                    case Direction.Down:
                        p = Faces.Bottom, 0, self.position.y, Direction.Down
                    case Direction.Left:
                        p = (
                            Faces.Left,
                            self.N - 1,
                            self.N - self.position.x - 1,
                            Direction.Up,
                        )
            case Faces.Bottom:
                match to:
                    case Direction.Up:
                        p = Faces.Down, self.N - 1, self.position.y, Direction.Up
                    case Direction.Right:
                        p = (
                            Faces.Right,
                            self.N - self.position.x - 1,
                            self.N - 1,
                            Direction.Left,
                        )
                    case Direction.Down:
                        p = Faces.Up, 0, self.position.y, Direction.Down
                    case Direction.Left:
                        p = Faces.Left, self.N - self.position.x - 1, 0, Direction.Right

        assert p is not None
        return TurtlePosition(*p)

    def turn(self, direction: Direction):
        assert direction in (Direction.Left, Direction.Right)

        new_direction_angle = (self.position.direction.value + direction.value) % 360
        new_direction = Direction(new_direction_angle)

        self.position.direction = new_direction

    def walk(self, walls_block: bool = True):
        dx, dy = {
            Direction.Up: (-1, 0),
            Direction.Right: (0, 1),
            Direction.Down: (1, 0),
            Direction.Left: (0, -1),
        }[self.position.direction]

        nx, ny = self.position.x + dx, self.position.y + dy

        if nx < 0:
            p = self._transition(Direction.Up)
        elif ny < 0:
            p = self._transition(Direction.Left)
        elif nx >= self.N:
            p = self._transition(Direction.Down)
        elif ny >= self.N:
            p = self._transition(Direction.Right)
        else:
            # stay within this face
            p = TurtlePosition(self.position.face, nx, ny, self.position.direction)

        self.position = p

        if walls_block and self.get().material == Material.Rock:
            # turn right around
            self.turn(Direction.Left)
            self.turn(Direction.Left)
            self.walk(walls_block=True)
            self.turn(Direction.Left)
            self.turn(Direction.Left)

    def get(self) -> CubePosition:
        return self.faces[self.position.face][self.position.x][self.position.y]

    def set_(
        self,
        material: Material,
        original_x: int,
        original_y: int,
        original_direction: Direction,
    ) -> None:
        self.faces[self.position.face][self.position.x][self.position.y] = CubePosition(
            material, original_x, original_y, original_direction
        )

    def __init__(self, N: int, data: list[list[str]]):

        # shape of the cube
        #   U
        #  LFR
        #   D
        #   B

        empty_face = [
            [CubePosition(Material.UNSET, -1, -1, Direction.Right) for _ in range(N)]
            for _ in range(N)
        ]
        self.faces = {f: copy.deepcopy(empty_face) for f in Faces}

        self.N = N
        start_position = TurtlePosition(Faces.Face, 0, 0, Direction.Right)
        self.position = start_position

        data_x = 0
        data_y = min(data[data_x].index("."), data[data_x].index("#"))

        self._init_neighbours(data_x, data_y, data)

        print(self.position)

    def _init_neighbours(self, data_x: int, data_y: int, data: list[list[str]]):

        if (
            data_x < 0
            or data_y < 0
            or data_x >= len(data)
            or data_y >= len(data[data_x])
            or data[data_x][data_y] == " "
        ):
            return
        # if self.get().material != Material.UNSET:
        #     assert self.get().material == Material(data[data_x][data_y])
        #     return

        already_set = False
        for x in range(self.N):

            # scan right
            for y in range(self.N):

                if self.get().material != Material.UNSET:
                    already_set = True
                    assert self.get() == CubePosition(
                        Material(data[data_x + x][data_y + y]),
                        data_x + x,
                        data_y + y,
                        self.position.direction,
                    )
                else:
                    self.set_(
                        Material(data[data_x + x][data_y + y]),
                        data_x + x,
                        data_y + y,
                        self.position.direction,
                    )
                self.walk(False)
            self.turn(Direction.Right)
            self.turn(Direction.Right)
            for y in range(self.N):
                self.walk(False)
            self.turn(Direction.Right)
            self.turn(Direction.Right)

            # go down one
            self.turn(Direction.Right)
            self.walk(False)
            self.turn(Direction.Left)

        # return up x
        self.turn(Direction.Left)
        for x in range(self.N):
            self.walk(False)
        self.turn(Direction.Right)

        if already_set:
            return

        if data_y - self.N >= 0 and data[data_x][data_y - self.N] != " ":
            # go left block
            self.turn(Direction.Right)
            self.turn(Direction.Right)
            for _ in range(self.N):
                self.walk(False)
            self.turn(Direction.Right)
            self.turn(Direction.Right)

            self._init_neighbours(data_x, data_y - self.N, data)

            for _ in range(self.N):
                self.walk(False)

        if data_y + self.N < len(data[data_x]):
            for _ in range(self.N):
                self.walk(False)

            self._init_neighbours(data_x, data_y + self.N, data)

            self.turn(Direction.Right)
            self.turn(Direction.Right)
            for _ in range(self.N):
                self.walk(False)
            self.turn(Direction.Right)
            self.turn(Direction.Right)

        if (
            data_x + self.N < len(data)
            and data_y < len(data[data_x + self.N])
            and data[data_x + self.N][data_y] != " "
        ):
            self.turn(Direction.Right)
            for _ in range(self.N):
                self.walk(False)
            self.turn(Direction.Left)

            self._init_neighbours(data_x + self.N, data_y, data)

            self.turn(Direction.Left)
            for _ in range(self.N):
                self.walk(False)
            self.turn(Direction.Right)

        return


Instruction = namedtuple("Instruction", ["steps", "turn"])


def split_instruction_str(instruction_str: str):
    instruction_str += "X"
    instructions = list()
    i = 0
    for j in range(len(instruction_str)):
        if instruction_str[j] in ("L", "R", "X"):

            steps = instruction_str[i:j]
            turn = instruction_str[j]

            steps = int(steps)
            match turn:
                case "L":
                    turn = Direction.Left
                case "R":
                    turn = Direction.Right
                case "X":
                    turn = None
                case _:
                    assert False

            instructions.append(Instruction(steps, turn))

            i = j + 1

    return instructions


def main(data: str) -> int:
    data = data.splitlines()
    # '#' - wall
    # '.' - open
    # 'x' - wrap

    instructions = data.pop(-1)
    assert data.pop(-1) == ""
    # N is the side length of the cube
    # I think the map always has to have one row, with 'length' == N

    N = min([row.count(".") + row.count("#") for row in data])

    cubeTurtle = CubeTurtle(N, data)
    print(cubeTurtle)

    for steps, turn in split_instruction_str(instructions):

        for _ in range(steps):
            cubeTurtle.walk()

        if turn:
            cubeTurtle.turn(turn)

    final_point = cubeTurtle.get()

    final_data_x, final_data_y = final_point.original_x, final_point.original_y
    original_direction = final_point.original_facing
    final_direction = cubeTurtle.position.direction

    final_direction = cubeTurtle.position.direction.value - (
        original_direction.value - Direction.Right.value
    )
    final_direction = Direction(final_direction)

    ans = 0
    x_points = (final_data_x + 1) * 1000
    y_points = (final_data_y + 1) * 4
    direction_points = {
        Direction.Right: 0,
        Direction.Down: 1,
        Direction.Left: 2,
        Direction.Up: 3,
    }[final_direction]

    ans = x_points + y_points + direction_points
    return ans


if __name__ == "__main__":

    data = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""
    from aocd import data, submit

    ret = main(data)

    print("ANSWER", ret)

    submit(ret)
