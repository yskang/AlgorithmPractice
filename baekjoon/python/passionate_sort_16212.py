# Title: 정열적인 정렬
# Link: https://www.acmicpc.net/problem/16212

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list):
    return sorted(ns)


def main():
    n = read_single_int()
    al = read_list_int()
    print(' '.join(map(str, solution(n, al))))


if __name__ == '__main__':
    main()