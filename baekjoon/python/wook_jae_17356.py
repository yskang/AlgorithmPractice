# Title: 욱 제
# Link: https://www.acmicpc.net/problem/17356

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a: int, b: int):
    m = (b-a)/400
    return 1/(1+pow(10, m))


def main():
    a, b = read_list_int()
    print(solution(a, b))


if __name__ == '__main__':
    main()