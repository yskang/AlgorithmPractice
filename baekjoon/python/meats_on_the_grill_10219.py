# Title: Meats On The Grill
# Link: https://www.acmicpc.net/problem/10219

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def flip_meat(grill):
    res = []
    for row in grill:
        row.reverse()
        res.append(''.join(row))
    return '\n'.join(res)


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        H, W = read_list_int()
        grill = []
        for _ in range(H):
            grill.append(list(sys.stdin.readline().strip()))
        print(flip_meat(grill))