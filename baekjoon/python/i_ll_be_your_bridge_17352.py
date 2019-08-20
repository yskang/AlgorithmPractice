# Title: 여러분의 다리가 되어 드리겠습니다.
# Link: https://www.acmicpc.net/problem/17352

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
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


def solution(n: int, bridges: list):
    uf = UnionFind(n+1)
    for a, b in bridges:
        uf.union(a, b)
    
    base = uf.find(1)
    for i in range(1, n+1):
        if uf.find(i) != base:
            return '{} {}'.format(1, i)


def main():
    n = read_single_int()
    bridges = []
    for _ in range(n-2):
        bridges.append(read_list_int())
    print(solution(n, bridges))


if __name__ == '__main__':
    main()