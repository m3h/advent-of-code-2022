#!/usr/bin/env python3
from dataclasses import dataclass
from collections import defaultdict
import re
import time


def compare(a, b):
    if type(a) == int and type(b) == int:
        if a < b:
            return -1
        elif a == b:
            return 0
        elif a > b:
            return 1
    elif type(a) == list and type(b) == list:
        c = 0
        for i in range(min(len(a), len(b))):
            c = compare(a[i], b[i])
            if c == -1:
                return -1
            elif c == 0:
                pass
            elif c == 1:
                return 1
        if len(a) < len(b):
            return -1
        elif len(a) == len(b):
            return 0
        elif len(a) > len(b):
            return 1
        

    elif type(a) == int:
        return compare([a], b)
    elif type(b) == int:
        return compare(a, [b])
    
    


def main(data: str):

    data = data.splitlines()

    s = 0
    for i in range(0, len(data), 3):
        a_s = data[i]
        b_s = data[i+1]

        a = eval(a_s)
        b = eval(b_s)

        if compare(a, b) != 1:
            idx = i // 3 + 1
            s += idx
            print(idx, a, b)
    return s

    ans = 0

    return ans

if __name__ == "__main__":


    data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


    # from aocd import data, submit
    # data = data.splitlines()
    ret = main(data)

    print('ANSWER',ret)

    # submit(ret)
