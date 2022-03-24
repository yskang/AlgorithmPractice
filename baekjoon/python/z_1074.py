# Title: Z
# Link: https://www.acmicpc.net/problem/1074

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_visit(N, y, x):
    width = 2**N

    start = 0
    end = width**2-1
    quarter = width**2//4

    offset = [[0, 1], [2, 3]]

    while end-start != 3:
        half_width = width//2
        if y < half_width and x < half_width:
            end = start + quarter - 1
        elif y < half_width <= x:
            start += quarter
            end = start + quarter - 1
            x -= half_width
        elif y >= half_width > x:
            start += 2 * quarter
            end = start + quarter - 1
            y -= half_width
        else:
            start += 3 * quarter
            end = start + quarter - 1
            x -= half_width
            y -= half_width
        quarter = quarter // 4
        width = half_width

    return start+offset[y][x]


if __name__ == '__main__':
    N, r, c = read_list_int()
    print(get_visit(N, r, c))