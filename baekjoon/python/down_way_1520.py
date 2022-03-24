# Title: 내리막 길 
# Link: https://www.acmicpc.net/problem/1520

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_ways(maps, w, h):
    dp = [[0]*w for _ in range(h)]

    dp[0][0] = 1
    for x in range(1, w):
        if maps[0][x] < maps[0][x-1]:
            dp[0][x] += dp[0][x-1]

    for y in range(1, h):
        for x in range(w):
            if maps[y][x] < maps[y][x-1]:
                dp[y][x] += dp[y][x-1]
            if maps[y][x] < maps[y-1][x]:
                dp[y][x] += dp[y-1][x]
            if x-1 >= 0 and maps[y][x] > maps[y][x-1]:
                dp[y][x-1] += dp[y][x]
    return dp[-1][-1]


if __name__ == '__main__':
    m, n = read_list_int()
    maps = []
    for _ in range(m):
        maps.append(read_list_int())
    print(get_ways(maps, n, m))