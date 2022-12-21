#!/usr/bin/env python3
from dataclasses import dataclass
from collections import defaultdict, namedtuple
import re
import time
import copy
import tqdm
from queue import PriorityQueue
import functools
import ast


def resolve_monkey(monkey_name: str, monkeys: dict[str, str | int]) -> int:
    monkey_op = monkeys[monkey_name]

    if type(monkey_op) == int:
        return monkey_op
    else:
        var_a, op, var_b = monkey_op.split()
        locals()[var_a] = resolve_monkey(var_a, monkeys)
        locals()[var_b] = resolve_monkey(var_b, monkeys)

        value = int(eval(monkey_op))
        monkeys[monkey_name] = value
        return resolve_monkey(monkey_name, monkeys)


def main(data: str) -> int:

    monkeys: dict[str, str] = dict()
    for data in data.splitlines():
        monkey_name, op = data.split(": ")
        try:
            op = int(op)
        except:
            pass

        monkeys[monkey_name] = op

    return resolve_monkey("root", monkeys)


if __name__ == "__main__":

    data = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

    # from aocd import data, submit

    ret = main(data)

    print("ANSWER", ret)

    submit(ret)
