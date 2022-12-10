#!/usr/bin/env python3
from dataclasses import dataclass


def check(X, cycle):
    if cycle >= 20 and (cycle - 20) % 40 == 0:
        print("XXX", X, cycle, X*cycle)
        return X * cycle
    return 0

# def draw_crt(crt, cycle, v):
#     i = cycle // 40
#     j = cycle % 40

#     crt[i][j] = v
def draw(crt, cycle, X):

    crt_i = (cycle - 1) % (40*6)
    crt_x = (cycle - 1) % (40)
    # crt_i = cycle % (40*60) - 1



    for i in range(X-1, X+1+1):
        if crt_x == i:
            crt[crt_i] = '#'

def main(data: str):

    # crt = [['X' for x in range(40)] for _ in  range(6)]
    crt = ['.' for x in range(40*6)]

    ans = 0

    X = 1
    cycle = 0

    i = 0
    # draw(crt, cycle, X)
    for line in data:
        if line == "noop":
            cycle += 1

            draw(crt, cycle, X)
        else:
            instr, val = line.split()
            val = int(val)

            cycle += 1
            draw(crt, cycle, X)

            cycle += 1
            draw(crt, cycle, X)
            X += val


        for i in range(0, len(crt), 40):
            x = crt[i:i+40]
            print(''.join(x))
        print()
        # print(line, X, cycle, ans) 



    return ans




if __name__ == "__main__":


    data = """noop
addx 3
addx -5"""

    data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

    # with open("input/full/day6/input.txt") as f:
    #     data = f.read()
    from aocd import data, submit
    data = data.splitlines()
    ret = main(data)

    print(ret)

    # submit(ret)
