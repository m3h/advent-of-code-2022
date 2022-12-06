#!/usr/bin/env python3


def main(data: str):

    for i in range(3, len(data)):
        if len({data[i], data[i-1], data[i-2], data[i-3]}) == 4:
            print(i)
            return i+1
    raise Exception()
    # ans = 0

    # print(ans)
    # return ans




if __name__ == "__main__":


    data = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

    # with open("input/full/day5/input.txt") as f:
    #     data = f.read()
    from aocd import data, submit
    # data = data.splitlines()
    ret = main(data)

    print(ret)

    submit(ret)
