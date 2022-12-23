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


Point = namedtuple("Point", ["x", "y"])


def count_smallest_ground(elves: set) -> int:
    min_x = min(elves, key=lambda elf: elf.x).x
    min_y = min(elves, key=lambda elf: elf.y).y

    max_x = max(elves, key=lambda elf: elf.x).x
    max_y = max(elves, key=lambda elf: elf.y).y

    x_size = max_x - min_x + 1
    y_size = max_y - min_y + 1

    rectangle_area = x_size * y_size
    ground_in_rectangle = rectangle_area - len(elves)
    return ground_in_rectangle


def print_elves(elves: set, highlighted: set = set()) -> None:
    min_x = min(elves, key=lambda elf: elf.x).x
    min_y = min(elves, key=lambda elf: elf.y).y

    max_x = max(elves, key=lambda elf: elf.x).x
    max_y = max(elves, key=lambda elf: elf.y).y

    x_size = max_x - min_x + 1
    y_size = max_y - min_y + 1

    grid = [(["."] * y_size) for _ in range(x_size)]

    for elf in elves:
        if elf in highlighted:
            grid[elf.x - min_x][elf.y - min_y] = "%"
        else:
            grid[elf.x - min_x][elf.y - min_y] = "#"

    if grid[0 - min_x][0 - min_y] == "#":
        grid[0 - min_x][0 - min_y] = "@"
    else:
        grid[0 - min_x][0 - min_y] = "-"

    for row in grid:
        print("".join(row))
    print()


def check_proposal(elf: Point, direction: Point, elves: set[Point]) -> None | Point:

    for sweep in (-1, 0, 1):
        if direction.y != 0:
            if Point(sweep + elf.x, direction.y + elf.y) in elves:
                # there is an elf in the way
                return None
        elif direction.x != 0:
            if Point(direction.x + elf.x, sweep + elf.y) in elves:
                # there is an elf in the way
                return None
        else:
            assert False

    if direction.y != 0:
        return Point(elf.x, elf.y + direction.y)
    elif direction.x != 0:
        return Point(elf.x + direction.x, elf.y)
    else:
        assert False


def count_around(elf: Point, elves: set[Point]) -> int:
    count = 0
    for sweep_x in (-1, 0, 1):
        for sweep_y in (-1, 0, 1):
            if Point(sweep_x + elf.x, sweep_y + elf.y) in elves:
                count += 1
    return count


def main(data: str) -> int:
    data = data.splitlines()

    elves = set()
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "#":
                elves.add(Point(x, y))

    proposal_checks = [
        lambda elf: check_proposal(elf, Point(-1, 0), elves),  # north
        lambda elf: check_proposal(elf, Point(1, 0), elves),  # south
        lambda elf: check_proposal(elf, Point(0, -1), elves),  # west
        lambda elf: check_proposal(elf, Point(0, 1), elves),  # east
    ]

    print("starting grid:")
    print_elves(elves)
    round_no = 0
    elves_moved = True
    while elves_moved:

        # first half of round
        # count proposals to go to Point
        proposals = defaultdict(list)

        elves_moved = False
        for elf in elves:
            if count_around(elf, elves) == 1:
                continue

            elves_moved = True
            for proposal_check in proposal_checks:
                p = proposal_check(elf)
                if p is not None:
                    proposals[p].append(elf)
                    break

        # second half of round
        for proposal_point, proposer_elves in proposals.items():
            if len(proposer_elves) > 1:
                continue
            else:
                assert len(proposer_elves) == 1
                elves.remove(proposer_elves[0])
                elves.add(proposal_point)

        round_no += 1
        print(f"== End of Round {round_no} ==")
        print_elves(elves)
        proposal_checks = proposal_checks[1:] + [proposal_checks[0]]

        if round_no == 10:
            return count_smallest_ground(elves)

    assert False
    return


if __name__ == "__main__":

    #     data = """.....
    # ..##.
    # ..#..
    # .....
    # ..##.
    # ....."""

    data = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""

    from aocd import data, submit

    ret = main(data)

    print("ANSWER", ret)

    submit(ret)
