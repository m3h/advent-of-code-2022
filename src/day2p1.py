#!/usr/bin/env python3


def read_input(fpath):
    with open(fpath) as f:
        return f.readlines()


def main(fpath: str):
    data = read_input(fpath)
    print(data)
    data = [x.strip().split() for x in data]

    score = 0
    for him, me in data:
        print(him, me)

        scores = {
            "X": 1,
            "Y": 2,
            "Z": 3,
        }
        score += scores[me]
        # A rock b paper c scissors
        # x rock y paper z scissors
        if him == "A":
            if me == "X":
                score += 3
            if me == "Y":
                score += 6

        if him == "B":
            if me == "Y":
                score += 3
            if me == "Z":
                score += 6
        if him == "C":
            if me == "Z":
                score += 3
            if me == "X":
                score += 6

        print(score)


if __name__ == "__main__":

    input_type = "test"
    input_type = "full"
    fpath = f"./input/{input_type}/day2/input.txt"

    main(fpath)
