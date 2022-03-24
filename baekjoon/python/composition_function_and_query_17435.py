# Title: 합성합수와 쿼리
# Link: https://www.acmicpc.net/problem/17435

import sys
import math


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(m: int, fs: list, q: int, queries: list):
    dp = [[-1 for _ in range(m+1)] for _ in range(20)]

    for f, t in enumerate(fs, 1):
        dp[1][f] = t
    
    for i in range(2, 20):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][dp[i-1][j]]

    for n, s in queries:
        while n:
            k = n & ~(n-1)
            s = dp[int(math.log2(k)+1)][s]
            n -= k
        print(s)


def main():
    m = read_single_int()
    fs = read_list_int()
    q = read_single_int()
    queries = []
    for _ in range(q):
        queries.append(read_list_int())
    solution(m, fs, q, queries)


if __name__ == '__main__':
    main()