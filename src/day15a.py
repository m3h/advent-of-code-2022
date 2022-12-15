#!/usr/bin/env python3
from dataclasses import dataclass
from collections import defaultdict
import re
import time
import copy
import tqdm


def main(data: str):
    data = data.splitlines()

    covered = list()
    beacons = list()
    signals = list()
    for line in data:
        _, _, sx, sy, _, _, _, _, bx, by = line.split()
        sx = int(sx[2:-1])
        sy = int(sy[2:-1])
        bx = int(bx[2:-1])
        by = int(by[2:])

        signals.append((sx, sy))
        beacons.append((bx, by))

    covered = set()
    y = 10
    # y = 2000000
    for i in range(len(signals)):
        dsb = abs(beacons[i][0] - signals[i][0]) + abs(beacons[i][1] - signals[i][1])

        dy = abs(signals[i][1] - y)
        dx = dsb - dy

        if dx <= 0:
            continue

        print(dy, dx, signals[i], beacons[i])
        for x in range(-dx, dx + 1):
            x += signals[i][0]
            covered.add(x)

    for i in range(len(beacons)):
        if beacons[i][1] == y:
            x = beacons[i][0]
            if x in covered:
                covered.remove(x)

    return len(covered)

    leftmost_beacon = sorted(beacons + signals, key=lambda x: x[0])[0]
    rightmost_beacon = sorted(beacons + signals, key=lambda x: x[0])[-1]

    ans = 0
    y = 2000000
    for x in tqdm.tqdm(range(leftmost_beacon[0], rightmost_beacon[0] + 1)):

        if (x, y) in beacons:
            continue

        isnt = True
        for i in range(len(signals)):
            dsb = abs(beacons[i][0] - signals[i][0]) + abs(
                beacons[i][1] - signals[i][1]
            )
            dsx = abs(x - signals[i][0]) + abs(y - signals[i][1])

            if dsx <= dsb:
                # print("isnt", (x, y), signals[i], beacons[i])
                isnt = False
                break
                # isn't
        if not isnt:
            # print("nd", x, y)
            ans += 1
    return ans


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

    # from aocd import data, submit

    ret = main(data)

    print("ANSWER", ret)

    # submit(ret)
4560025
