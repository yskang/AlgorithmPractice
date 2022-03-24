# Title: 수열의 합
# Link: https://www.acmicpc.net/problem/1024

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_sequence(n, ll):
    for l in range(ll, 101):
        if (n/l + 1/2 -l/2).is_integer():
            s = n//l - (l-1)//2
            if s < 0:
                continue
            ns = [x for x in range(s, s+l)]
            return ns
        elif (n/l + 1/2 -l/2) <= 0:
            return [-1]
    return [-1]


if __name__ == '__main__':
    n, l = read_list_int()
    print(' '.join(map(str, get_sequence(n, l))))