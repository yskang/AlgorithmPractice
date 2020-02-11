# Title: 쿼리와 쿼리
# Link: https://www.acmicpc.net/problem/18254

import sys


sys.setrecursionlimit(10 ** 6)
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0 for _ in range(n+1)]
    
    def _update(self, p: int, v: int):
        while p <= self.n:
            self.bit[p] ^= v
            p += (p & (-p))

    def _query(self, b: int):
        s = 0
        while b > 0:
            s ^= self.bit[b]
            b -= (b & (-b))
        return s

    def update_range(self, l: int, r: int, v: int):
        self._update(l, v)
        self._update(r+1, v)

    def query_point(self, p: int):
        return self._query(p)


def solution(n: int, m: int, q: int, a_list: list, updates: list, queries: list):
    prefix_xors = [0]

    for a in a_list:
        prefix_xors.append(prefix_xors[-1]^a)

    bit = BIT(n)

    ans = []

    for query in queries:
        if query[0] == 1:
            bit.update_range(query[1], query[2], query[3])
        else:
            ql, qr = query[1], query[2]
            res = prefix_xors[qr] ^ prefix_xors[ql-1]
            for i in range(m):
                l, r, x = updates[i]
                if r < ql or qr < l:
                    continue
                if (min(r, qr) - max(l, ql) + 1) % 2:
                    res ^= bit._query(i+1) ^ x
            ans.append(str(res))
    return '\n'.join(ans)


def main():
    n, m, q = read_list_int()
    a_list = read_list_int()

    updates = []
    queries = []
    for _ in range(m):
        updates.append(read_list_int())
    for _ in range(q):
        queries.append(read_list_int())
    print(solution(n, m, q, a_list, updates, queries))


if __name__ == '__main__':
    main()