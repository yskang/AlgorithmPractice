# Title: 무한 수열
# Link: https://www.acmicpc.net/problem/1351

import sys
from math import floor
from collections import defaultdict as ddict

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_a(n: int, p: int, q: int, cache):
    if cache[n] != -1:
        return cache[n]
    if n == 0:
        cache[0] = 1
        return 1
    a = get_a(floor(n/p), p, q, cache) + get_a(floor(n/q), p, q, cache)
    cache[n] = a
    return a


def solution(n: int, p: int, q: int):
    cache = ddict(lambda: -1)
    return get_a(n, p, q, cache)


def main():
    n, p, q = read_list_int()
    print(solution(n, p, q))


if __name__ == '__main__':
    main()