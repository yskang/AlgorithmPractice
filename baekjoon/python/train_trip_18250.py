# Title: 철도 여행
# Link: https://www.acmicpc.net/problem/18250

import sys
from collections import defaultdict

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


def solution(n: int, m: int, rails: list, uf: UnionFind):
    groups = defaultdict(lambda: [])
    for i in range(1, n+1):
        groups[uf.find(i)].append(i)

    trips = 0

    for name in groups:
        trips += 1
        odds = 0
        for station in groups[name]:
            if len(groups[name]) == 1:
                trips -= 1
                continue
            if len(rails[station]) % 2 == 1:
                odds += 1
        if odds >= 4:
            trips += (odds-2)//2
    return trips


def main():
    n, m = read_list_int()
    uf = UnionFind(n+1)
    rails = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = read_list_int()
        rails[u].append(v)
        rails[v].append(u)
        uf.union(u, v)
    print(solution(n, m, rails, uf))


if __name__ == '__main__':
    main()