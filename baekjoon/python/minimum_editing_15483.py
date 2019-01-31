# Title: 최소 편집
# Link: https://www.acmicpc.net/problem/15483

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().rstrip()


def solution(a: str, b: str):
    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    dp[0] = [i for i in range(len(a)+1)]

    for y in range(1, len(b)+1):
        for x in range(len(a)+1):
            if x == 0:
                dp[y][x] = y
            elif a[x-1] == b[y-1]:
                dp[y][x] = dp[y-1][x-1]
            else:
                dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1])+1

    return dp[len(b)][len(a)]


def main():
    a = read_single_str()
    b = read_single_str()
    print(solution(a, b))


if __name__ == '__main__':
    main()