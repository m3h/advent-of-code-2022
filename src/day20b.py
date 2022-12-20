#!/usr/bin/env python3
import dataclasses
import tqdm
import functools
from collections import defaultdict
import re
import math


@dataclasses.dataclass
class Number:
    v: int

    def __eq__(self, other):
        return id(self) == id(other)

    def __repr__(self):
        return str(self.v)


def sgn(x: int) -> int:
    return type(x)(math.copysign(1, x))


def swap(idx_a: int, idx_b: int, arr: list):
    tmp = arr[idx_a]
    arr[idx_a] = arr[idx_b]
    arr[idx_b] = tmp


def mix(original_data: list[Number], mixed_data: list[Number]) -> None:
    for number in original_data:
        movement = number.v
        movement = (abs(movement) % (len(mixed_data) - 1)) * sgn(movement)
        # print(movement)

        direction, magnitude = sgn(movement), abs(movement)

        current_idx = mixed_data.index(number)
        new_idx = (abs(current_idx + movement) % (len(mixed_data) - 1)) * sgn(movement)

        for _ in range(magnitude):
            new_idx = (current_idx + direction) % len(mixed_data)
            swap(current_idx, new_idx, mixed_data)
            current_idx = new_idx

            # print(_, mixed_data)
        # print(mixed_data)
        # print()


# def mix(original_data: list[Number], mixed_data: list[Number]) -> None:
#     for number in original_data:
#         movement = number.v

#         current_idx = mixed_data.index(number)

#         if movement < 0:
#             movement -= 1
#         new_idx = (current_idx + movement) % len(mixed_data)

#         # if new_idx > current_idx:
#         #     new_idx -= 1
#         del mixed_data[current_idx]
#         mixed_data.insert(new_idx, number)

#         print(mixed_data)


def main(data: str) -> int:

    data = map(int, data.splitlines())
    data = map(lambda x: x * 811589153, data)
    data = list(map(Number, data))

    mixed_data = list(data)
    # inplace mix
    for _ in tqdm.tqdm(range(10)):
        mix(data, mixed_data)

    ans = 0
    zero_offset = [d.v == 0 for d in mixed_data].index(True)

    for grove_coord_idx in (1000, 2000, 3000):
        ans += mixed_data[(zero_offset + grove_coord_idx) % len(mixed_data)].v
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
    # submit(answer)
