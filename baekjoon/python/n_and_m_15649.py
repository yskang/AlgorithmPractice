# Title: N과 M(1)
# Link: https://www.acmicpc.net/problem/15649

import sys
from itertools import permutations


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int):
    for sub in permutations([i+1 for i in range(n)], m):
        print(*sub)


def main():
    n, m = read_list_int()
    solution(n, m)


if __name__ == '__main__':
    main()