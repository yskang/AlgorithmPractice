# Title: 최대공약수와 최소공배수
# Link: https://www.acmicpc.net/problem/2609

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b, gcd_val):
    return a * b // gcd_val


if __name__ == '__main__':
    a, b = read_list_int()
    gcd_val = gcd(a, b)
    print(gcd_val)
    print(lcm(a, b, gcd_val))