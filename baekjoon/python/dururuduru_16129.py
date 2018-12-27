# Title: 뚜루루 뚜루
# Link: https://www.acmicpc.net/problem/16129

import sys
import collections
import copy


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dururuduru = ['r', 'r', 'd', 'r']

def dfs(m: list, x: int, y: int, width: int, height: int, depth: int, ox: int, oy: int):
    if depth == 4:
        return 1
    count = 0
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if not(ox == nx and oy == ny) and 0 <= nx < width and 0 <= ny < height and m[ny][nx] == dururuduru[depth]:
            count += dfs(m, nx, ny, width, height, depth+1, x, y)
    return count


def get_paths(m: list, x: int, y: int, width: int, height: int):
    count = 0
    count += dfs(m, x, y, width, height, 0, -1, -1)
    return count


def solution(r: int, c: int):
    m = [['N' for _ in range(c)] for _ in range(r)]
    ds = []

    s = collections.deque()

    s.append('d')
    s.append('r')
    s.append('r')
    s.append('d')
    s.append('r')

    for y, row in enumerate(m):
        for x, _ in enumerate(row):
            row[x] = s[0]
            if s[0] == 'd':
                ds.append((x, y))
            s.rotate(-1)

    count = 0
    for x, y in ds:
        count += dfs(m, x, y, c, r, 0, -1, -1)

    return count


def main():
    r, c = read_list_int()
    print(solution(r, c))


if __name__ == '__main__':
    main()