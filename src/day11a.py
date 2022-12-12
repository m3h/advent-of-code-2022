#!/usr/bin/env python3
from dataclasses import dataclass
from collections import defaultdict
import re

class Monkey:
    def __init__(self, number, starting_items, operation, test_val, true_action, false_action):
        self.number = number
        self.items = starting_items
        self.operation = operation
        self.test_val = test_val
        self.true_action = true_action
        self.false_action = false_action
        self.inspections = 0

def main(data: str):

    cur_no = None
    # monkeys = dict()
    monkeys = list()

    i = 0
    while i < len(data):
        monkey_no = int(data[i].split()[1][:-1])
        _, item_str = data[i+1].split(':')
        items = [int(x) for x in item_str.split(',')]
        operation = data[i+2].split(':')[1].split('=')[1]
        test = int(data[i+3].split()[-1])
        true_monkey = int(data[i+4].split()[-1])
        false_monkey = int(data[i+5].split()[-1])

        i += 7

        m = Monkey(monkey_no, items, operation, test, true_monkey, false_monkey)
        monkeys.append(m)

    for i in range(20):
        for M in monkeys:
            while len(M.items) > 0:
                M.inspections += 1
                old = M.items.pop(0)
                worry = eval(M.operation)
                worry = worry // 3
                if worry % M.test_val == 0:
                    monkeys[M.true_action].items.append(worry)
                else:
                    monkeys[M.false_action].items.append(worry)

        print("Round", i+1)
        for M in monkeys:
            print(f"Monkey {M.number}: {M.items}")
        print()
    
    inspections = [M.inspections for M in monkeys]
    inspections.sort(reverse=True)
    print(inspections)
    return inspections[0] * inspections[1]
    ans = 0






    return ans




if __name__ == "__main__":


    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


    # with open("input/full/day6/input.txt") as f:
    #     data = f.read()
    # from aocd import data, submit
    data = data.splitlines()
    ret = main(data)

    print(ret)

    # submit(ret)
