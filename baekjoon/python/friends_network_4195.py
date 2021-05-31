# Title: 친구 네트워크
# Link: https://www.acmicpc.net/problem/4195

import sys
from collections import defaultdict

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_words = lambda: sys.stdin.readline().strip().split(' ')

class UnionFind:
    def __init__(self):
        self.groups = defaultdict(lambda : set())

    def find(self, a: int):
        if len(self.groups[a]) != 0:
            return a
        self.groups[a].add(a)
        return a

    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)
        if self.groups[a] != self.groups[b]:
            self.groups[a].update(self.groups[b])
            self.groups[b] = self.groups[a]


def solution(f: int, network: list):
    uf = UnionFind()
    for a, b in network:
        uf.union(a, b)
        print(len(uf.groups[a]))


def main():
    t = read_single_int()
    for _ in range(t):
        f = read_single_int()
        uf = UnionFind()
        for _ in range(f):
            a, b = read_list_words()
            uf.union(a, b)
            print(len(uf.groups[a]))


if __name__ == '__main__':
    main()