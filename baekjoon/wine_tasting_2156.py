# Title: Wine Tasting (포도주 시식) 
# Link: https://www.acmicpc.net/problem/2156

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_max_wine(wines):
    d1 = [0] * len(wines)
    d2 = [0] * len(wines)
    s = [0] * len(wines)

    d1[0] = wines[0]
    d2[0] = 0
    s[0] = 0
    for n, wine in enumerate(wines[1:], 1):
        d1[n] = s[n-1] + wine
        d2[n] = d1[n-1] + wine
        s[n] = max(s[n-1], d1[n-1], d2[n-1])

    return max(d1[-1], d2[-1], s[-1])


if __name__ == '__main__':
    n = read_single_int()
    wines = []
    for _ in range(n):
        wines.append(read_single_int())
    print(get_max_wine(wines))