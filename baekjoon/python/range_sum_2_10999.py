# Title: 구간 합 구하기 2
# Link: https://www.acmicpc.net/problem/10999

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class BIT:
    def __init__(self, n):
        self.n = n
        self.bit1 = [0 for _ in range(n+1)]
        self.bit2 = [0 for _ in range(n+1)]
    
    def _update(self, ft: list, p: int, v: int):
        while p <= self.n:
            ft[p] += v
            p += (p & (-p))

    def update_range(self, a: int, b: int, v: int):
        self._update(self.bit1, a, v)
        self._update(self.bit1, b+1, -v)
        self._update(self.bit2, a, v*(a-1))
        self._update(self.bit2, b+1, -v*b)

    def _query(self, ft: list, b: int):
        s = 0
        while b > 0:
            s += ft[b]
            b -= (b & (-b))
        return s

    def query(self, b: int):
        return self._query(self.bit1, b) * b - self._query(self.bit2, b)
    
    def query_range(self, a: int, b: int):
        return self.query(b) - self.query(a-1)


def solution(n: int, m: int, k: int, ns: list, qs: list):
    b_sums = [0 for _ in range(n+1)]
    for i, a in enumerate(ns, 1):
        b_sums[i] = b_sums[i-1] + a

    bit = BIT(n)
    for q in qs:
        if q[0] == 1:
            bit.update_range(q[1], q[2], q[3])
        elif q[0] == 2:
            s = bit.query_range(q[1], q[2])
            print(b_sums[q[2]] - b_sums[q[1]-1] + s)


def main():
    n, m, k = read_list_int()
    ns = []
    for _ in range(n):
        ns.append(read_single_int())
    qs = []
    for _ in range(m+k):
        qs.append(read_list_int())
    solution(n, m, k, ns, qs)


if __name__ == '__main__':
    main()