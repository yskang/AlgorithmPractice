# Title: 최소 스패닝 트리
# Link: https://www.acmicpc.net/problem/1197

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

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


def solution(v: int, e: int, edges: list):
    uf = UnionFind(v+1)
    costs = 0
    edges = sorted(edges, key=lambda x: x[2])
    for a, b, c in edges:
        if uf.find(a) != uf.find(b):
            costs += c
            uf.union(a, b)
    return costs


def main():
    v, e = read_list_int()
    edges = []
    for _ in range(e):
        edges.append(read_list_int())
    print(solution(v, e, edges))


if __name__ == '__main__':
    main()