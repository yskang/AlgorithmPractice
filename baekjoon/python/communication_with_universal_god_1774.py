# Title: 우주신과의 교감
# Link: https://www.acmicpc.net/problem/1774

import sys
from math import sqrt


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


def solution(n: int, m: int, gods: list, channels: list):
    ans = 0
    uf = UnionFind(n+1)
    for a, b in channels:
        uf.union(a, b)
    
    god_channels = []
    for i in range(n):
        for j in range(i+1, n):
            god_channels.append((i+1, j+1, (gods[i][0]-gods[j][0])**2+(gods[i][1]-gods[j][1])**2))
    god_channels = sorted(god_channels, key=lambda x: x[2])

    for a, b, d in god_channels:
        if uf.find(a) != uf.find(b):
            ans += sqrt(d)
            uf.union(a, b)
    return '{:.2f}'.format(ans)


def main():
    n, m = read_list_int()
    gods = []
    channel = []
    for _ in range(n):
        gods.append(read_list_int())
    for _ in range(m):
        channel.append(read_list_int())
    print(solution(n, m, gods, channel))


if __name__ == '__main__':
    main()