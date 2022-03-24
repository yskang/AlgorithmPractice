# Title: 트리 색칠하기
# Link: https://www.acmicpc.net/problem/1693

import sys

import collections

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)


def min_cost(node, color, color_limit, g_p, memos):
    cost = color
    for child in node.children:
        if child.name != g_p:
            costs = []
            for c in range(1, color_limit):
                if c != color:
                    if memos[(child.name, c)] == 0:
                        costs.append(min_cost(child, c, color_limit, node.name, memos))
                    else:
                        costs.append(memos[(child.name, c)])
            cost += min(costs)
    memos[(node.name, color)] = cost
    return cost


def get_cost(nodes):
    costs = []
    color_limit = 21
    memos = collections.defaultdict(lambda: 0)
    for color in range(1, color_limit):
        costs.append(min_cost(nodes[1], color, color_limit, -1, memos))
    return min(costs)


if __name__ == '__main__':
    n = read_single_int()
    nodes = {}

    for i in range(1, n+1):
        nodes[i] = Node(i)

    for _ in range(n - 1):
        a, b = read_list_int()
        nodes[a].add_child(nodes[b])
        nodes[b].add_child(nodes[a])

    print(get_cost(nodes))
