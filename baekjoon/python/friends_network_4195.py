# Title: 친구 네트워크
# Link: https://www.acmicpc.net/problem/4195

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_words = lambda: sys.stdin.readline().strip().split(' ')


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


def solution(f: int, network: list, friends: defaultdict):
    uf = UnionFind(f+1)
    for a, b in network:
        uf.union(friends[a], friends[b])
        print(uf.size(friends[a]))


def main():
    t = read_single_int()
    for _ in range(t):
        f = read_single_int()
        network = []
        number = 0
        friends = defaultdict(lambda: -1)
        for _ in range(f):
            a, b = read_list_words()
            if friends[a] == -1:
                friends[a] = number
                number += 1
            if friends[b] == -1:
                friends[b] = number
                number += 1
            network.append((a, b))
        solution(f, network, friends)


if __name__ == '__main__':
    main()