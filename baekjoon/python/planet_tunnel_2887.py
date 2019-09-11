# Title: 행성 터널
# Link: https://www.acmicpc.net/problem/2887

import sys
from collections import defaultdict


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


def solution(n: int, planets: list):
    tunnels = []

    for i in range(3):
        planets = sorted(planets, key=lambda x: x[i])
        prev_planet = planets[0]
        for planet in planets[1:]:
            tunnels.append((prev_planet[3], planet[3], min(abs(prev_planet[0]-planet[0]), abs(prev_planet[1]-planet[1]), abs(prev_planet[2]-planet[2]))))
            prev_planet = planet
    
    tunnels = sorted(tunnels, key= lambda x: x[2])

    total_cost = 0
    uf = UnionFind(n+1)

    for a, b, cost in tunnels:
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            total_cost += cost

    return total_cost


def main():
    n = read_single_int()
    planets = []
    for i in range(n):
        planets.append(read_list_int()+[i])
    print(solution(n, planets))


if __name__ == '__main__':
    main()