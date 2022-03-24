# Title: 별자리 만들기
# Link: https://www.acmicpc.net/problem/4386

import sys
from math import sqrt


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_float = lambda: list(map(float, sys.stdin.readline().strip().split(' ')))


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


def solution(n: int, stars: list):
    uf = UnionFind(n)
    cost = 0
    star_lines = []
    for i in range(n):
        for j in range(i+1, n):
            star_lines.append((i, j, (stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])**2))

    star_lines = sorted(star_lines, key=lambda x: x[2])

    for a, b, d in star_lines:
        if uf.find(a) != uf.find(b):
            cost += sqrt(d)
            uf.union(a, b)
    return cost


def main():
    n = read_single_int()
    stars = []
    for _ in range(n):
        stars.append(read_list_float())
    print(solution(n, stars))


if __name__ == '__main__':
    main()