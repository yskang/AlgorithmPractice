# Title: 피보나치 수 2
# Link: https://www.acmicpc.net/problem/

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def fibonacci(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]


if __name__ == '__main__':
    dp = [0] * 91
    dp[1] = 1
    for i in range(2, 91):
        dp[i] = dp[i-1]+dp[i-2]

    n = read_single_int()
    print(dp[n])