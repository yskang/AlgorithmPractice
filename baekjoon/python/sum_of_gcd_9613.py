# Title: GCD 합
# Link: https://www.acmicpc.net/problem/9613

import sys
import itertools


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def gcd(a: int, b: int):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def solution(ns: list):
    return sum([gcd(x, y) for (x, y) in itertools.combinations(ns[1:], 2)])


def main():
    t = read_single_int()
    for _ in range(t):
        ns = read_list_int()
        print(solution(ns))


if __name__ == '__main__':
    main()