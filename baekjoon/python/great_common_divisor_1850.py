# Title: 최대공약수
# Link: https://www.acmicpc.net/problem/1850

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def gcd(a, b):
    (a, b) = (a, b) if a <= b else (b, a)
    while b != 0:
        r = a % b
        a = b
        b = r
    return '1' * a


if __name__ == '__main__':
    a, b = read_list_int()
    print(gcd(a, b))