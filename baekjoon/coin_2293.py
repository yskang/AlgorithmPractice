# Title: coin 1 (동전 1) 
# Link: https://www.acmicpc.net/problem/2293

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def make_coin(coins, target):
    dp = [1] + [0] * target
    for coin in coins:
        for n in range(1, target+1):
            if n >= coin:
                dp[n] += dp[n - coin]
    return dp[target]


if __name__ == '__main__':
    n, k = read_list_int()
    coins = []
    for _ in range(n):
        coins.append(read_single_int())
    print(make_coin(coins, k))
