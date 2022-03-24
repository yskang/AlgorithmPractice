# Title: 공항
# Link: https://www.acmicpc.net/problem/10775

import sys
from copy import deepcopy


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


class MaxSegment:
    def __init__(self, ns: list, n: int):
        self.n = n
        self.tree = [0 for _ in range(n)] + deepcopy(ns) + [0]
        for i in range(n-1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
    
    def update(self, pos: int, value: int):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos >>= 1
            self.tree[pos] = max(self.tree[2*pos], self.tree[2*pos+1])

    def range_query(self, left: int, right: int):
        left += self.n
        right += 1
        right += self.n
        ma = -(10**10)
        while left < right:
            if left & 1 != 0:
                ma = max(ma, self.tree[left])
                left += 1
            if right & 1 != 0:
                right -= 1
                ma = max(ma, self.tree[right])
            left //= 2
            right //= 2
        return ma


def solution(g: int, p: int, gs: list):
    gates = [i for i in range(g+1)]
    tree = MaxSegment(gates, g+1)
    count = 0
    for gate in gs:
        available = tree.range_query(1, gate)
        if available <= 0:
            return count
        tree.update(available, -available)
        count += 1

    return count


def main():
    g = read_single_int()
    p = read_single_int()
    gs = []
    for _ in range(p):
        gs.append(read_single_int())
    print(solution(g, p, gs))


if __name__ == '__main__':
    main()