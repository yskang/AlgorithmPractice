# Title: 분해합
# Link: https://www.acmicpc.net/problem/2231

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_sum(n):
    for creator in range(max(1, n-54), n):
        s = creator
        for c in str(creator):
            s += int(c)
        if n == s:
            return creator
    return 0


if __name__ == '__main__':
    n = read_single_int()
    print(get_sum(n))