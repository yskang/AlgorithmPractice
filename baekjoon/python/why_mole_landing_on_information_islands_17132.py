# Title: 두더지가 정보섬에 올라온 이유
# Link: https://www.acmicpc.net/problem/17132

import sys
from itertools import combinations


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class UnionFind:
    def __init__(self, max_count):
        self.p = [-1 for _ in range(max_count+1)]

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


def solution(n: int, edges: list):
    edges = sorted(edges, reverse=True)
    uf = UnionFind(100000)
    result = 0
    for w, u, v in edges:
        result += w * uf.size(u) * uf.size(v)
        uf.union(u, v)
    return result


def main():
    n = read_single_int()
    edges = []
    for _ in range(n-1):
        a, b, w = read_list_int()
        edges.append((w, a, b))

    print(solution(n, edges))


if __name__ == '__main__':
    main()