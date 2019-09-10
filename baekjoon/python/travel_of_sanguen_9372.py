# Title: 상근이의 여행
# Link: https://www.acmicpc.net/problem/9372

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


def solution(n: int, m: int, airlines: list):
    count = 0
    uf = UnionFind(n+1)
    for a, b in airlines:
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            count += 1
    return count


def main():
    t = read_single_int()
    for _ in range(t):
        n, m = read_list_int()
        airlines = []
        for _ in range(m):
            a, b = read_list_int()
            airlines.append((a, b))
        print(solution(n, m, airlines))


if __name__ == '__main__':
    main()