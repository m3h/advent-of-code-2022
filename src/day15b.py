#!/usr/bin/env python3
from dataclasses import dataclass
from collections import defaultdict, namedtuple
import re
import time
import copy
import tqdm

Point = namedtuple("Point", "x y")


def l1(p1: Point, p2: Point):
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)


def check(signals, covered_d, p, upper_bound):
    if p.x < 0 or p.y < 0 or p.x > upper_bound or p.y > upper_bound:
        return False

    for signal, cov_d in zip(signals, covered_d):
        dist_sp = l1(signal, p)
        if dist_sp <= cov_d:
            return False
    return True


def tuning_freq(p: Point):
    return p.x * 4000000 + p.y


def main(data: str, upper_bound):
    data = data.splitlines()
    # parallel list
    signals = list()
    beacons = list()
    covered_d = list()
    curr_search_distances = list()
    for line in data:
        m = re.match(
            r"Sensor at x=([-+]?\d+), y=([-+]?\d+): closest beacon is at x=([-+]?\d+), y=([-+]?\d+)",
            line,
        )
        sx, sy, bx, by = m.groups()

        signal = Point(int(sx), int(sy))
        beacon = Point(int(bx), int(by))
        d = l1(signal, beacon)

        signals.append(signal)
        beacons.append(beacon)
        covered_d.append(d)
        curr_search_distances.append(d + 1)

    for i in tqdm.tqdm(range(len(signals))):
        # generate circle around signal
        signal = signals[i]
        sd = curr_search_distances[i]

        # x_min = max(0, signal.x - sd)
        # x_max = min(upper_bound, signal.x + sd)

        # for x in tqdm.tqdm(range(x_min, x_max + 1)):
        for dx in tqdm.tqdm(range(-sd, sd + 1)):
            for dy_sign in (-1, 1):
                dy_abs = sd - dx
                if dy_abs < 0:
                    continue
                dy = dy_abs * dy_sign

                p = Point(signal.x + dx, signal.y + dy)
                if check(signals, covered_d, p, upper_bound):
                    return tuning_freq(p)
        # increase circle radius
        curr_search_distances[i] += 1

    return "not found"


if __name__ == "__main__":

    data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
    upper_bound = 20

    from aocd import data, submit

    upper_bound = 4000000

    ret = main(data, upper_bound=upper_bound)

    print("ANSWER", ret)

    submit(ret)
4560025
