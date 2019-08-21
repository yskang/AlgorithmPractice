# Title: 자동차가 차주 김표준의 편을 들면?
# Link: https://www.acmicpc.net/problem/17357

import sys

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
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


def solution(n: int, ns: list):
    sq_ns = list(map(lambda x: x*x, ns))
    bit_ns = Fenwick(ns)
    bit_sq_ns = Fenwick(sq_ns)

    res = []
    for k in range(1, -~n):
        max_sigma = -9999
        ans = 1
        for s in range(n):
            if s+k > n:
                break

            summ = bit_ns.sum(s, s+k-1)
            sqr_sum = bit_sq_ns.sum(s, s+k-1)

            sigma = sqr_sum*k - (summ**2)

            if max_sigma < sigma:
                max_sigma = sigma
                ans = s+1
        res.append(ans)
    return '\n'.join(map(str, res))


def main():
    n = read_single_int()
    ns = read_list_int()
    print(solution(n, ns))


if __name__ == '__main__':
    main()