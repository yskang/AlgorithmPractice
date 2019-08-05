# Title: 유기농 배추
# Link: https://www.acmicpc.net/problem/1012

import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(width: int, height: int, num_cabbages: int, land: list, cabbages: list):
    ans = 0
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for x, y in cabbages:
        if land[y][x] == 1:
            q = deque()
            q.append((x, y))
            while q:
                xx, yy = q.popleft()
                if land[yy][xx] == 0:
                    continue
                land[yy][xx] = 0
                for offset_x, offset_y in offsets:
                    if 0 <= xx+offset_x < width and 0 <= yy+offset_y < height and land[yy+offset_y][xx+offset_x]:
                        q.append((xx+offset_x, yy+offset_y))
            ans += 1
    return ans
    

def main():
    t = read_single_int()
    for _ in range(t):
        width, height, num_cabbages = read_list_int()
        land = [[0 for _ in range(width)] for _ in range(height)]
        cabbages = []
        for _ in range(num_cabbages):
            x, y = read_list_int()
            cabbages.append((x, y))
            land[y][x] = 1
        print(solution(width, height, num_cabbages, land, cabbages))


if __name__ == '__main__':
    main()