#!/usr/bin/env python3
from dataclasses import dataclass
from collections import defaultdict
import re


def min_dist(Q, dist):
    min_i, min_d = None, float('inf')
    for i, v in enumerate(Q):
        if dist[v[0]][v[1]] <= min_d:
            min_d = dist[v[0]][v[1]]
            min_i = i
    
    return Q.pop(min_i)

def valid_neighbour(v, u, Q, m, neighbours):
    if v[0] < 0 or v[1] < 0 or v[0] >= len(m) or v[1] >= len(m[0]):
        return
    if v not in Q:
        return
    # if ord(m[v[0]][v[1]]) - ord(m[u[0]][u[1]]) > 1:
    if ord(m[u[0]][u[1]]) - ord(m[v[0]][v[1]]) > 1:
        return
    
    neighbours.append(v)


def valid_neighbours(u, Q, m):
    neighbours = list()
    valid_neighbour((u[0]-1, u[1]), u, Q, m, neighbours)
    valid_neighbour((u[0], u[1]+1), u, Q, m, neighbours)
    valid_neighbour((u[0]+1, u[1]), u, Q, m, neighbours)
    valid_neighbour((u[0], u[1]-1), u, Q, m, neighbours)
    return neighbours

def dijkstra(m, start, goal):

    dist = [[float('inf') for y in range(len(m[0]))] for x in range(len(m))]
    prev = [[None for y in range(len(m[0]))] for x in range(len(m))]
    Q = list()
    for x in range(len(m)):
        for y in range(len(m[0])):
            Q.append((x, y))
    dist[start[0]][start[1]] = 0

    while len(Q) > 0:
        u = min_dist(Q, dist)
        for v in valid_neighbours(u, Q, m):
            # d = ord(m[v[0]][v[1]]) - ord(m[u[0]][u[1]])
            d = 1
            alt = dist[u[0]][u[1]] + d
            if alt < dist[v[0]][v[1]]:
                dist[v[0]][v[1]] = alt
                prev[v[0]][v[1]] = u

    min_d = float('inf')
    min_i = None
    for x in range(len(m)):
        for y in range(len(m[0])):
            if m[x][y] == 'a':
                if dist[x][y] < min_d:
                    min_d = dist[x][y]
                    min_i = x, y
    return min_d
    return dist[goal[0]][goal[1]]


def main(data: str):
    ans = 0

    m = list()
    start = None
    goal = None
    for x, line in enumerate(data.splitlines()):
        m.append(list())
        for y, char in enumerate(line):
            if char == 'S':
                start = (x,y)
                char = 'a'
            elif char == 'E':
                goal = (x, y)
                char = 'z'
            
            # v = ord(char) - ord('a')
            m[-1].append(char)
    
    for x in range(len(m)):
        for y in range(len(m[x])):
            print(m[x][y], end='')
        print()

    cost = dijkstra(m, goal=start, start=goal)

    return cost
    # print(paths)
    # return min(paths)



if __name__ == "__main__":


    data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


    # with open("input/full/day6/input.txt") as f:
    #     data = f.read()
    from aocd import data, submit
    # data = data.splitlines()
    ret = main(data)

    print(ret)

    submit(ret)
