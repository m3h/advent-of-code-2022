#!/usr/bin/env python3
from dataclasses import dataclass
from collections import defaultdict
import re
import time
import copy


def draw_section(graph):

    tgraph = graph[480 : 553 + 1][0 : 100 + 1]

    def transpose(l1):
        l2 = [[row[i] for row in l1] for i in range(len(l1[0]))]
        return l2

    print()
    for line in transpose(tgraph):
        print("".join(line))
    print()


def sgn(x):
    return x and (1, -1)[x < 0]


def fall(graph, sand, iters, lmx, rmx, lmy):
    iters += 1

    # if sand[1] + 1 > lmy:
    # return iters, True
    if graph[sand[0]][sand[1] + 1] == ".":
        return fall(graph, (sand[0], sand[1] + 1), iters, lmx, rmx, lmy)
    # elif sand[0] - 1 < lmx:
    # return iters, True
    elif graph[sand[0] - 1][sand[1] + 1] == ".":
        return fall(graph, (sand[0] - 1, sand[1] + 1), iters, lmx, rmx, lmy)
    # elif sand[0] + 1 > rmx:
    # return iters, True
    elif graph[sand[0] + 1][sand[1] + 1] == ".":
        return fall(graph, (sand[0] + 1, sand[1] + 1), iters, lmx, rmx, lmy)
    else:
        # rest, now
        graph[sand[0]][sand[1]] = "o"
        return iters, False


def main(data: str):

    # return ans
    dirs = list()
    for lin in data.splitlines():
        dirs.append(list())
        points = lin.split(" -> ")
        for point in points:
            x, y = point.split(",")
            x, y = int(x), int(y)

            dirs[-1].append((x, y))

    sand_source = 500, 0

    lmx, lmy = float("inf"), float("-inf")
    rmx, rmy = float("-inf"), float("-inf")
    for ps in dirs:
        for x, y in ps:
            if x < lmx:
                lmx = x
            elif x > rmx:
                rmx = x
            if y > lmy or y > rmy:
                lmy = y
                rmy = y

    print("lm", lmx, lmy)
    print("rm", rmx, rmy)

    graph = [["." for _ in range(2 * lmy + 1 + 2)] for _ in range(2 * rmx + 1)]
    # graph = [(["."] * (lmy + 1))] * (rmx + 1)
    for x in range(len(graph)):
        graph[x][lmy + 2] = "#"

    graph[500][0] = "+"

    for dir in dirs:
        for i in range(len(dir) - 1):

            dy = dir[i + 1][1] - dir[i][1]
            dx = dir[i + 1][0] - dir[i][0]

            dy = sgn(dy)
            dx = sgn(dx)

            p = dir[i]
            graph[p[0]][p[1]] = "#"
            while p != dir[i + 1]:
                p = p[0] + dx, p[1] + dy
                graph[p[0]][p[1]] = "#"

    sands = 0
    resting = True
    iters = 0
    while True:
        new_sand = (500, 0)
        new_iters, complete = fall(graph, new_sand, iters, lmx, rmx, lmy)

        if graph[500][0] == "o":
            return sands + 1
        else:
            sands += 1
        # if complete:
        #     return sands
        # else:
        #     iters = new_iters
        #     sands += 1

        # draw_section(graph)

    return sands


if __name__ == "__main__":

    data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

    from aocd import data, submit

    ret = main(data)

    print("ANSWER", ret)

    submit(ret)
