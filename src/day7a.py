#!/usr/bin/env python3
from dataclasses import dataclass

class Dir:
    def __init__(self, name, parent):
        self.children = list()
        self.name = name
        self.parent = parent
    
    def add_child(self, child):
        self.children.append(child)
    

    def sumsize(self):
        return sum([c.sumsize() for c in self.children])

    def __str__(self, pad=""):
        # thisd = pad + f"- {self.name} (dir)\n"
        # childlist = [c.__str__(pad=pad+" ") for c in self.children]
        return pad + f"- {self.name} (dir)\n" + ''.join([c.__str__(pad=pad+" ") for c in self.children])
    
    def __repr__(self):
        return self.__str__()

class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def __str__(self, pad=""):
        return pad + f"- {self.name} (file, size={self.size})\n"
    def __repr__(self):
        return self.__str__()
    
    def sumsize(self):
        return self.size

def main(data: str):

    ans = 0

    root = Dir(name='', parent=None)
    cur_dir = None

    for line in data:
        # print("processing line", line)
        # print(root)
        # print()

        line = line.split()
        if line[0] == '$':
            # command
            if line[1] == 'cd':
                if line[2] == '/':
                    cur_dir = root
                elif line[2] == '..':
                    cur_dir = cur_dir.parent
                else:
                    found = False
                    for child in cur_dir.children:
                        if child.name == line[2]:
                            cur_dir = child
                            found = True
                            break
                    if not found:
                        raise Exception
            
            elif line[1] == 'ls':
                # ignore for now
                pass

                # result of ls        
        else:
            if line[0] == 'dir':
                d = Dir(name=line[1], parent=cur_dir)
                cur_dir.children.append(d)
            else:
                f = File(name=line[1], size=int(line[0]), parent=cur_dir)
                cur_dir.children.append(f)


    print(root)

    ans = 0
    nodes = [root]
    while len(nodes) > 0:
        n = nodes.pop()
        s = n.sumsize()
        if s <= 100000:
            print(n.name, s)
            ans += s
        
        for c in n.children:
            if type(c) == Dir:
                nodes.insert(0, c)

    print("sum", ans)
    print(ans)
    return ans




if __name__ == "__main__":


    data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    # with open("input/full/day6/input.txt") as f:
    #     data = f.read()
    from aocd import data, submit
    data = data.splitlines()
    ret = main(data)

    print(ret)

    submit(ret)
