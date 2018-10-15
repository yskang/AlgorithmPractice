# Title: LCS(Longest Common Subsequence)
# Link: https://www.acmicpc.net/problem/9252

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_subsequence(a, b):
    dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]
    for y, sb in enumerate(b, 1):
        for x, sa in enumerate(a, 1):
            if sa == sb:
                dp[y][x] = dp[y-1][x-1] + 1
            else:
                dp[y][x] = max(dp[y-1][x], dp[y][x-1])
    max_len = dp[-1][-1]
    lcs = ''
    start = len(a)
    for y in range(len(b), 0, -1):
        for x in range(start, 0, -1):
            if dp[y][x] == max_len and dp[y][x-1] == dp[y-1][x-1] == dp[y-1][x] == max_len-1:
                max_len -= 1
                lcs = b[y-1] + lcs
                start = x
                break
    return lcs

if __name__ == '__main__':
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    lcs = get_subsequence(a, b)
    print(len(lcs))
    print(lcs)
