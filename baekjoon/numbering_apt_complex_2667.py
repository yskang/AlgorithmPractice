# Title: 단지번호붙이기
# Link: https://www.acmicpc.net/problem/2667

import sys

import collections

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def dfs(apt_map, x, y, visited, N):
    offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if visited[(x, y)]:
        return
    visited[(x, y)] = True
    apt_map[y][x] = 99999
    for offset in offsets:
        xx = x + offset[0]
        yy = y + offset[1]
        if 0 <= xx < N and 0 <= yy < N and apt_map[yy][xx] == 1:
            dfs(apt_map, xx, yy, visited, N)


def get_complex(apt_map, N):
    complexes = [0]
    visited = collections.defaultdict(lambda: False)
    for y, row in enumerate(apt_map):
        for x, house in enumerate(row):
            if house == 1:
                dfs(apt_map, x, y, visited, N)
                complexes.append(len(visited))
    res = []
    last = complexes[-1]
    for com in reversed(complexes[:-1]):
        res.append(last - com)
        last = com
    return '\n'.join(map(str, [len(res)] + sorted(res)))


if __name__ == '__main__':
    N = read_single_int()
    apt_map = []
    for _ in range(N):
        apt_map.append(list(map(int, sys.stdin.readline().strip())))
    print(get_complex(apt_map, N))