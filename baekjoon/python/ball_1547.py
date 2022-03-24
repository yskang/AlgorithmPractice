# Title: 공
# Link: https://www.acmicpc.net/problem/1547

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_cup_number(swaps):
    cups = {1:1, 2:2, 3:3}
    for x, y in swaps:
        cups[x], cups[y] = cups[y], cups[x]

    for x in cups:
        if cups[x] == 1:
            return x


if __name__ == '__main__':
    M = read_single_int()
    swaps = []
    for _ in range(M):
        X, Y = read_list_int()
        swaps.append((X, Y))
    print(get_cup_number(swaps))