# Title: 여행 가자
# Link: https://www.acmicpc.net/problem/1976

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


def solution(n: int, m: int, table: list, route: list):
    uf = UnionFind(n+1)
    for i, row in enumerate(table, 1):
        for j, city in enumerate(row, 1):
            if city == 1:
                uf.union(i, j)
    parent = uf.find(route.pop())
    while route:
        if parent != uf.find(route.pop()):
            return 'NO'
    return 'YES'


def main():
    n = read_single_int()
    m = read_single_int()
    table = []
    for _ in range(n):
        table.append(read_list_int())
    route = read_list_int()
    print(solution(n, m, table, route))


if __name__ == '__main__':
    main()