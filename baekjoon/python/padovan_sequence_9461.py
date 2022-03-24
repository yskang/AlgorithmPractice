# Title: 파도반 수열
# Link: https://www.acmicpc.net/problem/9461

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


if __name__ == '__main__':
    T = read_single_int()
    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    for x in range(90):
        p.append(p[-1]+p[-5])

    for _ in range(T):
        n = read_single_int()
        print(p[n])