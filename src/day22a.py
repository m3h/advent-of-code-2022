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

Instruction = namedtuple("Instruction", ["steps", "turn"])
Point = namedtuple("Point", ["x", "y", "direction"])


def split_instruction_str(instruction_str: str):
    instruction_str += "X"
    instructions = list()
    i = 0
    for j in range(len(instruction_str)):
        if instruction_str[j] in ("L", "R", "X"):

            steps = instruction_str[i:j]
            turn = instruction_str[j]

            instructions.append(Instruction(int(steps), turn))

            i = j + 1

    return instructions


directions = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}

markers = {
    "R": ">",
    "D": "v",
    "L": "<",
    "U": "^",
}


def step_next_point(
    map_: list[list[str]], cur: Point, steps: int, walked: list[list[str]]
) -> Point:

    x, y, _ = cur

    def inc(d):
        nonlocal x, y
        move = directions[cur.direction]

        x = (x + d * move[0]) % len(map_)
        y = (y + d * move[1]) % len(map_[0])

        walked[x] = list(walked[x])
        walked[x][y] = markers[cur.direction]

    for step in range(steps):
        inc(1)
        while map_[x][y] == "x" and map_[x][y] != "#":
            inc(1)

        if map_[x][y] == "#":
            # walk back one
            walked[x][y] = "#"
            inc(-1)
            while map_[x][y] == "x":
                inc(-1)

            return Point(x, y, cur.direction)

    return Point(x, y, cur.direction)


turn_angle = {"R": 90, "L": -90, "X": 0}
direction_angle = {"U": 0, "R": 90, "D": 180, "L": 270}
angle_direction = {v: k for k, v in direction_angle.items()}


def turn_next_point(cur: Point, turn):

    direction = cur.direction
    angle = direction_angle[direction]
    angle = (angle + turn_angle[turn]) % 360

    new_direction = angle_direction[angle]

    return Point(cur.x, cur.y, new_direction)


def walk(map_: list[list[str]], instructions: list[Instruction]):

    walked = copy.deepcopy(map_)
    # 1 for our 'x' padding
    current = Point(1, map_[1].index("."), "R")

    for steps, turn in instructions:

        current = step_next_point(map_, current, steps, walked)
        current = turn_next_point(current, turn)

        # print(steps, turn)
        # for row in walked:
        #     print("".join(row))
        # print("\n" * 5)

    return current


def main(data: str) -> int:
    data = data.splitlines()
    # '#' - wall
    # '.' - open
    # 'x' - wrap

    map_: list[list[str]] = list()
    instructions: str = None
    for row in data:
        if row == "":
            break
        row = row.replace(" ", "x")
        map_.append("x" + row + "x")

    max_cols = max([len(row) for row in map_])
    for i, row in enumerate(map_):
        map_[i] = row + "x" * (max_cols - len(row))
    instructions = data[-1]
    instructions = split_instruction_str(instructions)

    map_.insert(0, "x" * len(map_[0]))
    map_.append("x" * len(map_[-1]))
    for r in map_:
        print(r)
    print(instructions)

    current = walk(map_, instructions)

    facing_points = {"R": 0, "D": 1, "L": 2, "U": 3}
    ans = (current.x * 1000) + (current.y * 4) + facing_points[current.direction]
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
