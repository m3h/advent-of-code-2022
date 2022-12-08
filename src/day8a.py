#!/usr/bin/env python3
from dataclasses import dataclass


def main(data: str):

    visibles = set()
    treemap = list()
    for line in data:
        treemap.append([int(x) for x in list(line)])
    

    # scan left to right
    for i in range(len(treemap)):
        height = -1
        for j in range(len(treemap[i])):
            if treemap[i][j] > height:
                print((i, j))
                visibles.add((i, j))
                height = treemap[i][j]

    # right to left
    for i in range(len(treemap)):
        height = -1
        for j in range(len(treemap[i])-1, -1, -1):
            if treemap[i][j] > height:
                print((i, j))
                visibles.add((i, j))
                height = treemap[i][j]
    
    # up down 
    for j in range(len(treemap[0])):
        height = -1
        for i in range(len(treemap)-1, -1, -1):
            if treemap[i][j] > height:
                print((i, j))
                visibles.add((i, j))
                height = treemap[i][j]

    # down up 
    for j in range(len(treemap[0])):
        height = -1
        for i in range(0, len(treemap)):
            if treemap[i][j] > height:
                print((i, j))
                visibles.add((i, j))
                height = treemap[i][j]

    for visible in visibles:
        print(treemap[visible[0]][visible[1]])

    return len(visibles)
    return ans



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
