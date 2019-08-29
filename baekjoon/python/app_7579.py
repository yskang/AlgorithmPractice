# Title: 앱
# Link: https://www.acmicpc.net/problem/7579

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, ms: list, cs: list):
    ms = [0] + ms
    cs = [0] + cs
    total_cost = sum(cs)

    dp = [[0 for _ in range(total_cost+1)] for _ in range(n+1)]

    for app_index in range(1, n+1):
        for cost_limit in range(total_cost+1):
            dp[app_index][cost_limit] = max(dp[app_index-1][cost_limit],
                                            ms[app_index] + dp[app_index-1][cost_limit-cs[app_index]] if cost_limit-cs[app_index] >= 0 else 0)

    min_cost = 10**10

    for row in dp:
        for cost, memory in enumerate(row):
            if memory >= m:
                min_cost = min(min_cost, cost)
                continue
    return min_cost


def main():
    n, m = read_list_int()
    ms = read_list_int()
    cs = read_list_int()
    print(solution(n, m, ms, cs))


if __name__ == '__main__':
    main()