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

import operator

operator_lut = {
    "*": operator.mul,
    "/": operator.floordiv,
    "+": operator.add,
    "-": operator.sub,
}

solve_lhs = {
    "*": lambda b, y: y // b,
    "/": lambda b, y: y * b,
    "+": lambda b, y: y - b,
    "-": lambda b, y: y + b,
}

solve_rhs = {
    "*": lambda a, y: y // a,
    "/": lambda a, y: a // y,
    "+": lambda a, y: y - a,
    "-": lambda a, y: a - y,
}


class Operation:

    monkey_lut: dict[str, "Operation"] = dict()

    @classmethod
    def resolve(cls):
        for monkey in cls.monkey_lut.values():
            if isinstance(monkey.lhs, str):
                monkey.lhs = cls.monkey_lut[monkey.lhs]
            if isinstance(monkey.rhs, str):
                monkey.rhs = cls.monkey_lut[monkey.rhs]

    def __repr__(self):
        if self.int_value is not None:
            return str(self.int_value)
        else:
            return self.name

    def __init__(
        self, name: str, lhs: "Operation", op: str, rhs: "Operation", int_value: int
    ):
        self.name = name
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
        self.int_value = int_value

        self.monkey_lut[self.name] = self

    def value(self):

        if self.int_value is not None:
            return self.int_value
        elif self.lhs is None or self.rhs is None:
            return None
        elif self.op == "==":
            if self.lhs.value() is None:
                rhs_val = self.rhs.value()
                self.lhs.solve(rhs_val)
            elif self.rhs.value() is None:
                lhs_val = self.lhs.value()
                self.rhs.solve(lhs_val)

            return None

        elif self.lhs.value() is None or self.rhs.value() is None:
            return None
        else:
            self.int_value = operator_lut[self.op](self.lhs.value(), self.rhs.value())
            return self.value()

    def solve(self, y: int):

        if self.lhs is None and self.rhs is None and self.int_value is None:
            # this is a variable that needs a solvin'
            self.int_value = y
        elif self.lhs.value() is None:
            lhs_value = solve_lhs[self.op](self.rhs.value(), y)
            self.lhs.solve(lhs_value)
        elif self.rhs.value() is None:
            rhs_value = solve_rhs[self.op](self.lhs.value(), y)
            self.rhs.solve(rhs_value)
        else:
            assert False


def main(data: str) -> int:

    monkeys: dict[str, Operation] = dict()
    for data in data.splitlines():
        monkey_name, op = data.split(": ")
        try:
            int_value = int(op)
            lhs, op, rhs = None, None, None
        except:
            lhs, op, rhs = op.split()
            int_value = None

        monkey = Operation(monkey_name, lhs, op, rhs, int_value)
        monkeys[monkey_name] = monkey

    Operation.resolve()

    monkeys["humn"].int_value = None
    monkeys["root"].op = "=="
    # force a solvation
    monkeys["root"].value()
    return monkeys["humn"].int_value

    # return resolve_monkey("root", monkeys)


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

    from aocd import data, submit

    ret = main(data)

    print("ANSWER", ret)

    submit(ret)
