#!/usr/bin/env python3


def read_input(fpath):
    with open(fpath) as f:
        return f.readlines()

def contains(e1, e2):
    if e1[0] <= e2[0] and e2[1] <= e1[1]:
        return 1
    return 0
def main(data: str):
    data = [x.strip() for x in data]

    s = 0
    for pair in data:
        e1, e2 = pair.split(',')
        e1, e2 = e1.split('-'), e2.split('-')
        e1 = int(e1[0]), int(e1[1])
        e2 = int(e2[0]), int(e2[1])

        if e2[0] <= e1[1] and e2[1] >= e1[0] or e1[0] <= e2[1] and e1[1] >= e2[0]:
            s += 1
        # if e2[0] <= e1[1] or e1[0] <= e2[1]:
        #     s += 1

        # if contains(e1, e2) or contains(e2, e1):
        #     s += 1
        # s += contains(e1, e2)
        # continue
        # s += contains(e2, e1)
    print(s)


    s = 0


if __name__ == "__main__":


    data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    with open("input/full/day4/input.txt") as f:
        data = f.read()
    # from aocd import data, submit
    data = data.splitlines()
    ret = main(data)

    # submit(ret)
