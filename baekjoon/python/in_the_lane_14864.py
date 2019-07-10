# Title: 줄서기
# Link: https://www.acmicpc.net/problem/14864

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

class Fenwick:
    def __init__(self, array):
        self.array = array
        self.tree = [0 for _ in range(len(self.array)+1)]
        for i, a in enumerate(array):
            self.update(i, a)
    
    def update(self, i: int, diff: int):
        i += 1
        while i < len(self.tree):
            self.tree[i] += diff
            i += (i & -i)
    
    def _sum(self, i: int):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= (i & -i)
        return ans
    
    def sum(self, start: int, end: int):
        return self._sum(end+1) - self._sum(start)


def find_number(n: int, fenwick: Fenwick, m: int):
    left = 1
    right = m
    min_v = m+1
    while left <= right:
        middle = (left+right)//2
        if fenwick.sum(1, middle) < n:
            left = middle + 1
        else:
            min_v = min(min_v, middle)
            right = middle - 1   
    return min_v


def check_all(ns: list, pairs: list):
    for a, b in pairs:
        if ns[a] > ns[b]:
            continue
        return False
    return True


def solution(n: int, m: int, pairs: list):
    used = [1 for _ in range(n+1)]
    fenwick = Fenwick(used)
    behinds_of = [0 for _ in range(n+1)]
    for a, _ in pairs:
        behinds_of[a] += 1
    ans = [0]

    for i in range(1, n+1):
        x = find_number(behinds_of[i]+1, fenwick, n)
        ans.append(x)
        fenwick.update(x, -1)

    if check_all(ans, pairs):
        return ans[1:]
    return [-1]


def main():
    n, m = read_list_int()
    pairs = []
    for _ in range(m):
        pairs.append(read_list_int())
    print(*solution(n, m, pairs))


if __name__ == '__main__':
    main()