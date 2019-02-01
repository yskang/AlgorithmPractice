# Title: 동전 2
# Link: https://www.acmicpc.net/problem/2294

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


INF = 9999999999999


def get_count(k: int, coins: list, cache: list):
    if k == 0:
        return 0
    if cache[k] != -1:
        return cache[k]
    ret = INF
    for i in range(len(coins)):
        if k - coins[i] >= 0:
            ret = min(ret, 1 + get_count(k-coins[i], coins, cache))
    cache[k] = ret
    return ret


def solution(k: int, coins: set):
    cache = [-1 for _ in range(k+1)]
    ans = get_count(k, list(coins), cache)
    return -1 if ans == INF else ans


def main():
    n, k = read_list_int()
    coins = set()
    for _ in range(n):
        coins.add(read_single_int())
    print(solution(k, coins))


if __name__ == '__main__':
    main()