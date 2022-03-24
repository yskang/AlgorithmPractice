# Title: 북서풍
# Link: https://www.acmicpc.net/problem/5419

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0 for _ in range(n+1)]
    
    def update(self, p: int, v: int):
        while p <= self.n:
            self.bit[p] += v
            p += (p & (-p))

    def _query(self, b: int):
        s = 0
        while b > 0:
            s += self.bit[b]
            b -= (b & (-b))
        return s

    def query(self, a: int, b: int):
        return self._query(b) - self._query(a-1)


def solution(n: int, islands: defaultdict, xs: defaultdict):
    ans = 0
    bit = BIT(n+1)

    keys = sorted(islands.keys(), reverse=True)

    for key in keys:
        for x in sorted(islands[key]):
            ans += bit.query(1, xs[x])
            bit.update(xs[x], 1)

    return ans


def main():
    t = read_single_int()
    for _ in range(t):
        n = read_single_int()
        xs = defaultdict(lambda: -1)
        islands = defaultdict(lambda: [])
        for _ in range(n):
            x, y = read_list_int()
            xs[x] = 1
            islands[y].append(x)
        keys = sorted(xs.keys())
        for i, v in enumerate(keys, 1):
            xs[v] = i
        print(solution(n, islands, xs))


if __name__ == '__main__':
    main()