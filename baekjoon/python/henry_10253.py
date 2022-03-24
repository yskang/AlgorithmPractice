# Title: 헨리
# Link: https://www.acmicpc.net/problem/10253

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def make_henry_representation(a, b):
    while True:
        x = (b - 1) // a + 1
        a = a*x-b
        b = b*x
        if a == 0:
            return x


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        a, b = read_list_int()
        print(make_henry_representation(a, b))