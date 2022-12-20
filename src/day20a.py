#!/usr/bin/env python3
import dataclasses
import tqdm
import functools
from collections import defaultdict
import re


@dataclasses.dataclass
class Node:
    n: "Node"
    p: "Node"
    v: int
    processed: bool = False

    def __eq__(self, other):
        return id(self) == id(other)

    def __repr__(self):
        return f"({self.p.v}) > {self.v} > ({self.n.v})"

    def print_loop(self):
        node = self

        s = ""
        while id(node.n) != id(self):
            s += f"{node.v} -> "
            node = node.n
        s += f"{node.v} ->>> "
        return s


def init_linked_list(data: str) -> list[Node]:
    data = list(map(int, data.splitlines()))

    nodes: Node = [Node(None, None, v) for v in data]

    for i in range(1, len(nodes)):
        nodes[i - 1].n = nodes[i]
        nodes[i].p = nodes[i - 1]
    nodes[0].n = nodes[1]
    nodes[0].p = nodes[-1]
    nodes[-1].n = nodes[0]

    return nodes


def main(data: str) -> int:

    nodes = init_linked_list(data)
    head = nodes[0]
    print(head.print_loop())

    for n in tqdm.tqdm(nodes):
        for _ in range(abs(n.v)):
            nn = n.n
            np = n.p
            npn = n.p.n
            nnp = n.n.p
            nnn = n.n.n
            nnnp = n.n.n.p
            nppn = n.p.p.n
            npp = n.p.p

            if n.v > 0:
                np.n = nn
                nn.p = np
                nn.n = n
                n.p = nn
                n.n = nnn
                nnn.p = n
                if head == n:
                    head = n.p
            elif n.v < 0:
                npp.n = n
                n.p = npp
                n.n = np
                np.p = n
                np.n = nn
                nn.p = np
                if head == n:
                    head = n.n

        # print(n.v)
        # print(head.print_loop())
        # print()

    # find 0
    zero_node = head
    while zero_node.v != 0:
        zero_node = zero_node.n

    print(zero_node)

    # turn into list
    end_values = list()
    n = zero_node
    while n.n != zero_node:
        end_values.append(n.v)
        n = n.n
    end_values.append(n.v)

    print(end_values)

    ans = 0
    grove_indicies = [1000, 2000, 3000]
    for i in grove_indicies:
        v = end_values[i % len(end_values)]
        print(f"{i} -> {v}")
        ans += v
    return ans


if __name__ == "__main__":
    data = """1
2
-3
3
-2
0
4"""

    from aocd import data, submit

    answer = main(data)
    print(f"ANSWER: {answer}")
    submit(answer)
