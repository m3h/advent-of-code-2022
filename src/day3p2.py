#!/usr/bin/env python3


def read_input(fpath):
    with open(fpath) as f:
        return f.readlines()

def points(c: str):
    if c.lower() == c:
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

def main(data: str):
    data = [x.strip() for x in data]

    s = 0
    for i in range(0, len(data), 3):
        r1 = data[i]
        r2 = data[i+1]
        r3 = data[i+2]

        common = set(r1).intersection(set(r2)).intersection(set(r3))

        assert(len(common) == 1)

        print(points(list(common)[0]))

        s += points(list(common)[0])

    print("answer is ", s)

if __name__ == "__main__":


    data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    with open("input/full/day3/input.txt") as f:
        data = f.read()
    # from aocd import data, submit
    data = data.splitlines()
    ret = main(data)

    # submit(ret)
