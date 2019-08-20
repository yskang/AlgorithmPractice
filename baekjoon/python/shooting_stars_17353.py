# Title: 하늘에서 떨어지는 별
# Link: https://www.acmicpc.net/problem/17353

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class BinaryIndexTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0 for _ in range(n+1)]
    
    def _update(self, p: int, v: int):
        while p <= self.n:
            self.tree[p] += v
            p += (p & (-p))
    
    def update_range(self, start: int, end: int, value: int):
        self._update(start, value)
        self._update(end+1, -value)
    
    def query(self, p: int):
        s = 0
        while p > 0:
            s += self.tree[p]
            p -= (p & (-p))
        return s


def solution(n: int, ns: list, q: int, qs: list):
    bit_count = BinaryIndexTree(n)
    bit_starts = BinaryIndexTree(n)

    for query in qs:
        if query[0] == 1:
            bit_count.update_range(query[1], query[2], 1)
            bit_starts.update_range(query[1], query[2], query[1]-1)
        else:
            ans = ns[query[1]-1]
            count = bit_count.query(query[1])
            starts = bit_starts.query(query[1])
            print(ans + count * query[1] - (starts))


def main():
    n = read_single_int()
    ns = read_list_int()
    q = read_single_int()
    qs = []
    for _ in range(q):
        qs.append(read_list_int())
    solution(n, ns, q, qs)


if __name__ == '__main__':
    main()