#!/usr/bin/env python3


def main(data: str):
    # data = [x for x in data]

    # towers = list()
    towers = None
    i = 0
    while '[' in data[i]:
        chars = data[i][1::4]
        print(chars, len(chars))

        if towers is None:
            towers = list([] for x in range(len(chars)))
        for j, c in enumerate(chars):
            if c != ' ':
                towers[j].append(c)
        i += 1

    print(towers)
    i += 2
    for move in data[i:]:
        _, mc, _, mf, _, mt = move.split()
        print(move)
        print(mc, mf, mt)

        mf = int(mf) - 1
        mt = int(mt) - 1
        mc = int(mc)

        vs = towers[mf][0:mc]
        for j in range(mc):
            towers[mf].pop(0)
        for j in range(mc):
            towers[mt].insert(j, vs[j])
        
        print(towers)

    
    ans = [tower[0] for tower in towers]
    ans = ''.join(ans)
    print(ans)

    return ans




if __name__ == "__main__":


    data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    with open("input/full/day5/input.txt") as f:
        data = f.read()
    # from aocd import data, submit
    data = data.splitlines()
    ret = main(data)

    # submit(ret)
