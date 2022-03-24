# Title: 행복
# Link: https://www.acmicpc.net/problem/15969

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list):
    return max(ns)-min(ns)


def main():
    n = read_single_int()
    ns = read_list_int()
    print(solution(n, ns))


if __name__ == '__main__':
    main()