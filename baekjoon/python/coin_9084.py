# Title: 동전
# Link: https://www.acmicpc.net/problem/9084

import sys


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, coins: list, m: int):
    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(m+1):
            if i - coin >= 0:
                dp[i] += dp[i-coin]
    return dp[m]


def main():
    t = read_single_int()
    for _ in range(t):
        n = read_single_int()
        coins = read_list_int()
        m = read_single_int()
        print(solution(n, coins, m))


if __name__ == '__main__':
    main()