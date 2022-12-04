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

        if contains(e1, e2) or contains(e2, e1):
            s += 1
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

    with open("input/full/day4/input.txt") as f:
        data = f.read()
    # from aocd import data, submit
    data = data.splitlines()
    ret = main(data)

    # submit(ret)
