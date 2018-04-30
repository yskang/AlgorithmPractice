# Title: LCS(Longest Common Subsequence)
# Link: 9251

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
    return dp[-1][-1]
    # lcs = ''
    # x, y = len(a), len(b)
    # max_len = dp[y][x]
    # while max_len > 0:
    #     while dp[y][x] >= max_len:
    #         x -= 1
    #     lcs = a[x] + lcs
    #     y -= 1
    #     max_len -= 1
    # return lcs


if __name__ == '__main__':
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    print(get_subsequence(a, b))