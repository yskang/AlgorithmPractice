# Title: 최소공배수
# Link: https://www.acmicpc.net/problem/13241

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def gcm(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return a * b // gcm(a, b)


if __name__ == '__main__':
    a, b = read_list_int()
    print(lcm(a, b))