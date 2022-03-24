# Title: 집합의 표현
# Link: https://www.acmicpc.net/problem/1717

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


def solution(n: int, m: int, operations: list):
    uf = UnionFind(n+1)
    for op in operations:
        if op[0] == 0:
            uf.union(op[1], op[2])
        else:
            if uf.find(op[1]) == uf.find(op[2]):
                print('YES')
            else:
                print('NO')


def main():
    n, m = read_list_int()
    operations = []
    for _ in range(m):
        operations.append(read_list_int())
    solution(n, m, operations)


if __name__ == '__main__':
    main()