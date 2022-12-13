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
    
    

def bsort(arr):
    n= len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if compare(arr[j], arr[j+1]) == 1:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main(data: str):

    data = data.splitlines()

    # data += "[[2]]"
    # data += "[[6]]"

    s = 0

    packets = list()
    for i in range(0, len(data), 3):
        a_s = data[i]
        b_s = data[i+1]

        a = eval(a_s)
        b = eval(b_s)

        packets.append(a)
        packets.append(b)
    
    packets.append([[2]])
    packets.append([[6]])

    bsort(packets)
    # import functools
    # packets.sort(key = functools.cmp_to_key(compare))
    for p in packets:
        print(p)
    

    k1 = packets.index([[2]]) + 1
    k2 = packets.index([[6]]) + 1

    print("keys")
    print(k1, k2)
    return k1 * k2
    # ans = 0

    # return ans

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


    from aocd import data, submit
    # data = data.splitlines()
    ret = main(data)

    print('ANSWER',ret)

    submit(ret)
