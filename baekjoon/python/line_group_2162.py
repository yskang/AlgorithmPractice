# Title: 선분 그룹
# Link: https://www.acmicpc.net/problem/2162

import sys


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


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


def solution():
    uf = UnionFind(3001)
    for i, first_line in enumerate(lines):
        for second_line in lines[i+1:]:
            if is_met(first_line, second_line):
                uf.union(i, lines.index(second_line))
    return uf.size(0), uf.size(1)



def main():
    n = read_single_int()
    lines = []
    for _ in range(n):
        lines.append(read_list_int())
    print(solution(n, lines))


if __name__ == '__main__':
    main()