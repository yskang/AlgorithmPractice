# Title: 토끼가 정보섬에 올라온 이유
# Link: https://www.acmicpc.net/problem/17130

import sys
from collections import deque
from copy import deepcopy


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())

INF = 999999999999


def solution(rows: int, cols: int, islands: list):
    fields = []
    for row in islands:
        fields.append(list(map(lambda cell: 0 if cell == 'O' else -INF, row)))

    for c in range(cols-2, -1, -1):
        for r in range(0, rows):
            if islands[r][c] != '#':
                fields[r][c] = max(fields[r-1][c+1] if r-1 >= 0 else -INF, fields[r][c+1], fields[r+1][c+1] if r+1 < rows else -INF, fields[r][c]) + (1 if islands[r][c] == 'C' else 0)
            if islands[r][c] == 'R':
                return fields[r][c] if fields[r][c] >= 0 else -1
    return -1


def main():
    n, m = read_list_int()
    islands = []
    for _ in range(n):
        row = list(sys.stdin.readline().strip())
        islands.append(row)
    print(solution(n, m, islands))


if __name__ == '__main__':
    main()