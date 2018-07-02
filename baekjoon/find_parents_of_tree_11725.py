# Title: 트리의 부모 찾기
# Link: https://www.acmicpc.net/problem/11725

import sys

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


def dfs(node, parents, visited):
    visited[node.name] = True
    for child in node.children:
        if parents[child.name] == 0:
            parents[child.name] = node.name
        if not visited[child.name]:
            dfs(child, parents, visited)


def get_parents(node):
    parents = [0 for i in range(100001)]
    visited = [False for i in range(100001)]
    dfs(node, parents, visited)
    return parents


if __name__ == '__main__':
    N = read_single_int()
    nodes = {}
    for n in range(N):
        nodes[n+1] = Node(n+1)
    for _ in range(N-1):
        a, b = read_list_int()
        nodes[a].add_child(nodes[b])
        nodes[b].add_child(nodes[a])
    parents = get_parents(nodes[1])
    for i in range(2, N+1):
        print(parents[i])