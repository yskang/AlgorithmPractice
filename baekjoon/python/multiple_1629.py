# Title: 곱셈
# Link: https://www.acmicpc.net/problem/1629

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a: int, b: int, c: int):
    return pow(a, b, c)


def main():
    a, b, c = read_list_int()
    print(solution(a, b, c))


if __name__ == '__main__':
    main()