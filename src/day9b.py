#!/usr/bin/env python3
from dataclasses import dataclass

def move(h, t):
    mx = h[0] - t[0]
    my = h[1] - t[1]

    # if mx != 0:
    #     mx = 1
    # if my != 0:
    #     my = 1

    if abs(mx) <= 1 and abs(my) <= 1:
        # touching pass
        pass
    else:
        # not touching
        t[0] += (mx > 0) * 1 + (mx < 0) * -1
        t[1] += (my > 0) * 1 + (my < 0) * -1

    # print(h, t)

    # visited.append(tuple(t))
    # visited.add(tuple(t))

def main(data: str):
    ans = 0

    visited = list()

    knots = [[0, 0] for x in range(10)]
    # h = [0, 0]
    # t = [0, 0]
    for dir, steps in [x.split() for x in data]:
        print(dir, steps)

        steps = int(steps)
        while steps > 0:
            steps -= 1

            if dir == 'R':
                knots[0][0] += 1
            elif dir == 'L':
                knots[0][0] -= 1
            elif dir == 'U':
                knots[0][1] += 1
            elif dir == 'D':
                knots[0][1] -= 1
            

            for i in range(0, len(knots)-1):
                move(knots[i], knots[i+1])

            t = knots[-1] 
            visited.append(tuple(t))
            # visited.add(tuple(t))

    print(visited)
    return len(set(visited))
    return ans

if __name__ == "__main__":


    data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    # with open("input/full/day6/input.txt") as f:
    #     data = f.read()
    from aocd import data, submit
    data = data.splitlines()
    ret = main(data)

    print(ret)

    submit(ret)
