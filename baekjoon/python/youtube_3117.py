# Title: YouTube
# Link: https://www.acmicpc.net/problem/3117

import sys
from math import log2, ceil

sys.setrecursionlimit(10 ** 6)
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, k: int, m: int, firsts: list, recommends: list):
    z = ceil(log2(m))
    dp = [[-1 for _ in range(k+1)] for _ in range(z+2)]
    for i in range(1, k+1):
        dp[1][i] = recommends[i-1]

    for i in range(2, z+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][dp[i-1][j]]

    ans = []
    for first in firsts:
        t = m-1
        while t:
            c = t & ~(t-1)
            first = dp[int(log2(c))+1][first]
            t -= c
        ans.append(first)

    print(*ans)


def main():
    n, k, m = read_list_int()
    firsts = read_list_int()
    recommends = read_list_int()
    solution(n, k, m, firsts, recommends)


if __name__ == '__main__':
    main()