# Title: N과 M (2)
# Link: https://www.acmicpc.net/problem/1 5650

import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int):
    for ans in combinations([i+1 for i in range(n)], m):
        print(*ans)


def main():
    n, m = read_list_int()
    solution(n, m)


if __name__ == '__main__':
    main()