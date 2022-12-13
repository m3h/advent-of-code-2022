#!/usr/bin/env python3
import functools


def compare(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    elif type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            if c := compare(a[i], b[i]):
                return c
        return len(a) - len(b)
    elif type(a) == int:
        return compare([a], b)
    elif type(b) == int:
        return compare(a, [b])


def main():
    from aocd import data, submit

    data = data + "\n[[2]]\n[[6]]"
    packets = list(map(eval, data.split()))
    packets.sort(key=functools.cmp_to_key(compare))

    submit((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


if __name__ == "__main__":
    main()