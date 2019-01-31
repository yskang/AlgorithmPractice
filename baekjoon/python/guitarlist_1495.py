# Title: 기타리스트
# Link: https://www.acmicpc.net/problem/1495

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, s: int, m: int, v: list):
    dp = [{} for _ in range(n+1)]
    dp[0][s] = True

    for i in range(0, n):
        for x in dp[i].keys():
            if x-v[i] >= 0:
                dp[i+1][x-v[i]] = True
            if x+v[i] <= m:
                dp[i+1][x+v[i]] = True

    return sorted(dp[n].keys(), reverse=True)[0] if len(dp[n]) > 0 else -1


def main():
    n, s, m = read_list_int()
    v = read_list_int()
    print(solution(n, s, m, v))


if __name__ == '__main__':
    main()