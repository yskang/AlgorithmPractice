# Title: 달팽이는 올라가고 싶다
# Link: https://www.acmicpc.net/problem/2869

import sys
import math


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a: int, b: int, v: int):
    # a up, b down, v height
    return math.ceil((v-b)/(a-b))


def main():
    a, b, v = read_list_int()
    print(solution(a, b, v))


if __name__ == '__main__':
    main()