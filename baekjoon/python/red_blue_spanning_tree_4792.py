# Title: 레드 블루 스패닝 트리
# Link: https://www.acmicpc.net/problem/4792

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_words = lambda: sys.stdin.readline().strip().split(' ')


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


def solution(n: int, m: int, k: int, edges: list):
    minimum_k, maximum_k = 0, 0

    edges = sorted(edges, key=lambda x: x[0])

    uf_min = UnionFind(n+1)
    uf_max = UnionFind(n+1)
    
    for color, a, b in edges:
        if uf_max.find(a) != uf_max.find(b):
            if color == 'B':
                maximum_k += 1
            uf_max.union(a, b)

    for color, a, b in reversed(edges):
        if uf_min.find(a) != uf_min.find(b):
            if color == 'B':
                minimum_k += 1
            uf_min.union(a, b)
    
    if minimum_k <= k <= maximum_k:
        return 1
    return 0


def main():
    while True:
        n, m, k = read_list_int()
        if n == m == k == 0:
            break
        edges = []
        for _ in range(m):
            c, a, b = read_list_words()
            edges.append((c, int(a), int(b)))
        print(solution(n, m, k, edges))


if __name__ == '__main__':
    main()