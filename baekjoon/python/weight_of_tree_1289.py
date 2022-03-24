# Title: 트리의 가중치
# Link: https://www.acmicpc.net/problem/1289

import sys

import collections

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


mod = 1000000007


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, node, weight):
        self.children.append((node, weight))


def calc_weight(node, grand_node, weight):
    s = 1
    for (child, w) in node.children:
        if child.val != grand_node:
            total = calc_weight(child, node.val, weight)*w % mod
            weight[0] = (weight[0] + total * s) % mod
            s = (s+total) % mod
    return s


def get_weight(root):
    weight = [0]
    calc_weight(root, -1, weight)
    return weight[0]


if __name__ == '__main__':
    N = read_single_int()
    nodes = collections.defaultdict(lambda: None)
    for _ in range(N-1):
        A, B, W = read_list_int()
        if nodes[A] is None:
            nodes[A] = Node(A)
        if nodes[B] is None:
            nodes[B] = Node(B)
        nodes[A].add_child(nodes[B], W)
        nodes[B].add_child(nodes[A], W)
    print(get_weight(nodes[1]))