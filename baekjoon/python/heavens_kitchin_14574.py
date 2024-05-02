# Title: 헤븐스 키친
# Link: https://www.acmicpc.net/problem/14574

import sys
from itertools import combinations
from math import floor

sys.setrecursionlimit(10 ** 6)


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


class UnionFind:
    def __init__(self, max_count):
        self.p = [-1 for _ in range(max_count)]

    def find(self, a: int):
        if self.p[a] < 0:
            return a
        self.p[a] = self.find(self.p[a])
        return self.p[a]

    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.p[a] < self.p[b]:
            self.p[a] += self.p[b]
            self.p[b] = a
        else:
            self.p[b] += self.p[a]
            self.p[a] = b
        return True

    def size(self, a: int):
        return -self.p[self.find(a)]


def solution(n: int, cooks: list):
    uf = UnionFind(n+1)
    nums = [i for i in range(n)]
    battles = []
    for pair in combinations(nums, 2):
        a, b = pair
        ratio = floor((cooks[a][1]+cooks[b][1])/abs(cooks[a][0]-cooks[b][0]))
        battles.append((a, b, ratio))
    battles.sort(key=lambda x: x[2], reverse=True)

    graph = [[] for _ in range(n)]
    total_ratio = 0
    for a, b, r in battles:
        if uf.find(a) == uf.find(b):
            continue
        uf.union(a, b)
        graph[a].append(b)
        graph[b].append(a)
        total_ratio += r
    print(total_ratio)

    visits = [False for _ in range(n)]
    dfs(0, -1, graph, visits)


def dfs(node: int, from_node: int, graph: list, visits: list):
    if visits[node]:
        return
    visits[node] = True
    for next_node in graph[node]:
        if not visits[next_node]:
            dfs(next_node, node, graph, visits)
    if from_node != -1:
        print(f'{from_node+1} {node+1}')


def main():
    n = read_single_int()
    cooks = []
    for _ in range(n):
        cooks.append(read_list_int())
    solution(n, cooks)


if __name__ == '__main__':
    main()