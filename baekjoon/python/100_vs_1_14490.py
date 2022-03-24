# Title: 백대일
# Link: https://www.acmicpc.net/problem/14490

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(':')))


def gcd(a: int, b: int):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def solution(n: int, m: int):
    g = gcd(n, m)
    return '{}:{}'.format(n//g, m//g)


def main():
    n, m = read_list_int()
    print(solution(n, m))


if __name__ == '__main__':
    main()