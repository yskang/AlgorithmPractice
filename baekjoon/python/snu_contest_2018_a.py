# Title: 5차 전직
# Link: https://www.acmicpc.net/problem/16112

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, k: int, a: list):
    a = sorted(a)
    a = [0] + a
    exp = 0
    for i in range(2, k+1):
        exp += a[i] * (i-1)
    for i in range(k+1, n+1):
        exp += a[i] * k

    return exp


def main():
    n, k = read_list_int()
    a = read_list_int()
    print(solution(n, k, a))


if __name__ == '__main__':
    main()