import sys
import math
from typing import List

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def plog(s: str) -> None:
    print(s, file=sys.stderr, flush=True)


class Node:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score
        self.child_nodes = []
    
    def add_child(self, name:str, score: int):
        self.child_nodes.append(self.__class__(name, score))
    
    def get_child(self) -> List:
        return self.child_nodes
    
    def have_child(self, name: str):
        for child in self.child_nodes:
            if child.name == name:
                return child
        return None
    

def get_sum(node: Node) -> int:
    s = node.score
    for c in node.get_child():
        s += get_sum(c)
    return s


inputs = input().split()
plog(inputs)
n = int(inputs[0])
c = float(inputs[1])
ins = []
for i in range(n):
    inputs = input().split()
    plog(inputs)
    playout = inputs[0]
    score = float(inputs[1])
    ins.append(inputs)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

monte_tree = Node('root', 0)

for playout, score in ins:
    plog(f'{playout}, {score}')
    cur_node = monte_tree
    for node in playout:
        next_node = cur_node.have_child(node)
        if next_node:
            cur_node = next_node
        else:
            cur_node.add_child(node, score)
            break

# get best node
for node in monte_tree.get_child():
    get_sum(node)


print("aaaaa")
