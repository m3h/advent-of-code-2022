#!/usr/bin/env python3
from dataclasses import dataclass


def main(data: str):

    treemap = list()
    for line in data:
        treemap.append([int(x) for x in list(line)])
    

    hs = -1
    for si in range(len(treemap)):
        for sj in range(len(treemap[0])):


            # left            
            h1 = 0
            for i in  range(si-1, -1, -1):
                v = treemap[i][sj]
                x = treemap[si][sj]
                h1 += 1
                if treemap[i][sj] < treemap[si][sj]:
                    pass
                else:
                    break
            # right
            h2 = 0
            for i in  range(si+1, len(treemap), 1):
                v = treemap[i][sj]
                x = treemap[si][sj]
                h2 += 1
                if treemap[i][sj] < treemap[si][sj]:
                    pass
                else:
                    break
            # up
            h3 = 0
            for j in  range(sj+1, len(treemap[0]), 1):
                v = treemap[si][j]
                x = treemap[si][sj]
                h3 += 1
                if treemap[si][j] < treemap[si][sj]:
                    pass
                else:
                    break
            # down
            h4 = 0
            for j in  range(sj-1, -1, -1):
                v = treemap[si][j]
                x = treemap[si][sj]
                h4 += 1
                if treemap[si][j] < treemap[si][sj]:
                    pass
                else:
                    break

            s = h1*h2*h3*h4
            hs = max(s, hs)

            print(treemap[si][sj], s, h1, h2, h3, h4)

    return hs



if __name__ == "__main__":


    data = """30373
25512
65332
33549
35390"""

    # with open("input/full/day6/input.txt") as f:
    #     data = f.read()
    from aocd import data, submit
    data = data.splitlines()
    ret = main(data)

    print(ret)

    submit(ret)
