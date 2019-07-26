# Title: 손익분기점
# Link: https://www.acmicpc.net/problem/1712

import sys
import math

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a: int, b: int, c: int):
    if c-b <= 0:
        return -1
    if a/(c-b) == a//(c-b):
        return (a//(c-b)) + 1
    return math.ceil(a/(c-b))


def main():
    a, b, c = read_list_int()
    print(solution(a, b, c))


if __name__ == '__main__':
    main()