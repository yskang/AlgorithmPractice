# Title: 큰 수 A+B
# Link: https://www.acmicpc.net/problem/10757

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a: int, b: int):
    return a+b


def main():
    a, b = read_list_int()
    print(solution(a, b))


if __name__ == '__main__':
    main()