# Title: 작각다각형의 면적 구하기
# Link: https://www.acmicpc.net/problem/2620

import sys
from collections import deque


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))

    #  left top point is (0, 0) cell
    #      0  1  2  3  4  5  6  7  8  9
    #    0-+--+--------
    #      |00|
    #    1-+--+------
  
    #  top, right, bottom, left = 1, 2, 4, 8


def draw_lines(dots: list, land: list, r_map: list, c_map: list):
    dots.append(dots[0])
    prev_dot = dots[0]
    prev_dot = (r_map[prev_dot[0]], c_map[prev_dot[1]])
    for cur_dot in dots[1:]:
        cur_dot = (r_map[cur_dot[0]], c_map[cur_dot[1]])
        #  two dots are in the same row
        if prev_dot[0] == cur_dot[0]:
            r = prev_dot[0]
            min_c = min(prev_dot[1], cur_dot[1])
            max_c = max(prev_dot[1], cur_dot[1])
            for c in range(min_c, max_c):
                land[r][c] |= 1
        # two dots are in the same column
        elif prev_dot[1] == cur_dot[1]:
            c = prev_dot[1]
            min_r = min(prev_dot[0], cur_dot[0])
            max_r = max(prev_dot[0], cur_dot[0])
            for r in range(min_r, max_r):
                land[r][c] |= 8
        prev_dot = cur_dot


def get_area(land: list, r: int, c: int, zip_r: list, zip_c: list) -> int:
    area = 0
    queue = deque()
    queue.append((r, c))
    while queue:
        rr, cc = queue.popleft()
        if land[rr][cc] & 16 == 16:
            continue
        land[rr][cc] |= 16
        width = zip_c[cc+1] - zip_c[cc]
        height = zip_r[rr+1] - zip_r[rr]
        area += width * height
        # to right:
        nr = rr
        nc = cc+1
        if 0 <= nr < len(land)-1 and 0 <= nc < len(land[0])-1 and land[nr][nc] & 8 != 8 and land[nr][nc] & 16 != 16:
            queue.append((nr, nc))
        # to bottom:
        nr = rr+1
        nc = cc
        if 0 <= nr < len(land)-1 and 0 <= nc < len(land[0])-1 and land[nr][nc] & 1 != 1 and land[nr][nc] & 16 != 16:
            queue.append((nr, nc))
        # to left:
        nr = rr
        nc = cc-1
        if 0 <= nr < len(land)-1 and 0 <= nc < len(land[0])-1 and land[rr][cc] & 8 != 8 and land[nr][nc] & 16 != 16:
            queue.append((nr, nc))
        # to top:
        nr = rr-1
        nc = cc
        if 0 <= nr < len(land)-1 and 0 <= nc < len(land[0])-1 and land[rr][cc] & 1 != 1 and land[nr][nc] & 16 != 16:
            queue.append((nr, nc))
    return area


def solution(n: int, dots: list) -> int:
    max_area = 0
    zip_r = []
    zip_c = []
    r_map = [-1 for _ in range(10001)]
    c_map = [-1 for _ in range(10001)]

    for dot in dots:
        zip_r.append(dot[0])
        zip_c.append(dot[1])

    zip_r = sorted(list(set(zip_r)))
    zip_c = sorted(list(set(zip_c)))

    for i, r in enumerate(zip_r):
        r_map[r] = i
    for i, c in enumerate(zip_c):
        c_map[c] = i

    land = [[0 for _ in range(len(zip_c)+2)] for _ in range(len(zip_r)+2)]
    draw_lines(dots, land, r_map, c_map)

    zip_c.append(0)
    zip_c.append(0)
    zip_r.append(0)
    zip_r.append(0)
    for r in range(len(zip_r)-2, -1, -1):
        for c in range(len(zip_c)-2, -1, -1):
            if land[r][c] & 16 == 16:
                continue
            area = get_area(land, r, c, zip_r, zip_c)
            max_area = max(max_area, area)

    return max_area


def main():
    n = read_single_int()
    dots = []
    for _ in range(n):
        dots.append(read_list_int())
    print(solution(n, dots))


if __name__ == '__main__':
    main()