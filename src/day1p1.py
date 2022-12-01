#!/usr/bin/env python3


def read_input(fpath):
    with open(fpath) as f:
        return f.readlines()


def main(fpath: str):
    data = read_input(fpath)

    elves_calories = [0]

    for item in data:
        if item.strip() == "":
            elves_calories.append(0)
        else:
            elves_calories[-1] += int(item)

    print(max(elves_calories))


if __name__ == "__main__":

    input_type = "test"
    input_type = "full"
    fpath = f"./input/{input_type}/day1/input.txt"

    main(fpath)
