#!/usr/bin/env python3


def main(data: str):

    for i in range(14-1, len(data)):
        dataa = set([data[i-x] for x in range(14)])
        # print({data[i], data[i-1], data[i-2], data[i-3]})
        if len(dataa) == 14:
        # if len({data[i], data[i-1], data[i-2], data[i-3]}) == 14:
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
