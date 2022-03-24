# Title: 블랙잭
# Link: https://www.acmicpc.net/problem/2798

import sys
from itertools import combinations


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, cards: list):
    ans = 0
    for selects in combinations(cards, 3):
        s = sum(selects)
        if s == m:
            return m
        if s < m and s > ans:
            ans = s
    return ans


def main():
    n, m = read_list_int()
    cards = read_list_int()
    print(solution(n, m, cards))


if __name__ == '__main__':
    main()