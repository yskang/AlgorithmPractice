# Title: 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유
# Link: https://www.acmicpc.net/problem/17129

import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(rows: int, cols: int, floor: list, r: int, c: int):
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    floor[r][c] = 10
    q.append((r, c))
    while q:
        row, col = q.popleft()
        for offset in offsets:
            rr = row + offset[0]
            cc = col + offset[1]
            if 0<=rr<rows and 0<=cc<cols and floor[rr][cc] != 1 and floor[rr][cc] < 10:
                if 3 <= floor[rr][cc] <= 5:
                    return 'TAK\n{}'.format(floor[row][col] - 9)
                floor[rr][cc] = floor[row][col] + 1
                q.append((rr, cc))
    return 'NIE'


def main():
    n, m = read_list_int()
    floor = []
    r, c, = 0, 0
    for ri in range(n):
        row = list(map(int, sys.stdin.readline().strip()))
        floor.append(row)
        if 2 in row:
            c = row.index(2)
            r = ri

    print(solution(n, m, floor, r, c))


if __name__ == '__main__':
    main()