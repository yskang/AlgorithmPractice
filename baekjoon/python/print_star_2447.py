# Title: 별찍기 - 10
# Link: https://www.acmicpc.net/problem/2447

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def make_square(unit):
    width = len(unit)
    ans = [[' ' for _ in range(width * 3)] for _ in range(width * 3)]

    for y in range(3):
        for x in range(3):
            if x != 1 or y != 1:
                for uy in range(width):
                    for ux in range(width):
                        ans[y*width+ux][x*width+uy] = unit[ux][uy]

    return ans


def print_star(N):
    unit = [['*']]
    while len(unit) != N:
        unit = make_square(unit)
    for line in unit:
        print(''.join(line))


if __name__ == '__main__':
    N = read_single_int()
    print_star(N)


