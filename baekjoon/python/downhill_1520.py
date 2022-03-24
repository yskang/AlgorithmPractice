# Title: 내리막 길
# Link: https://www.acmicpc.net/problem/1520

import sys

sys.setrecursionlimit(10 ** 6)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def in_map(x, y, w, h):
    if x < 0 or y < 0 or x >= w or y >= h:
        return False
    return True


def move(x, y, geo, dp, w, h):
    if x == w-1 and y == h-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
        if in_map(next_x, next_y, w, h) and geo[next_y][next_x] < geo[y][x]:
            dp[y][x] += move(next_x, next_y, geo, dp, w, h)
    return dp[y][x]


def find_ways(geo, width, height):
    dp = [[-1]*width for _ in range(height)]

    move(0, 0, geo, dp, width, height)
    return dp[0][0]


if __name__ == '__main__':
    m, n = read_list_int()
    geo = []
    for _ in range(m):
        geo.append(read_list_int())
    print(find_ways(geo, n, m))
