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
    for rucksack in data:
        print(rucksack, len(rucksack)//2)
        com1 = rucksack[:len(rucksack)//2]
        com2 = rucksack[len(rucksack)//2:]
        print(com1, com2)

        common = set(com1).intersection(set(com2))

        print(common)

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
