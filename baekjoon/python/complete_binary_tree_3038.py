# Title: 완전 이진 트리
# Link: https://www.acmicpc.net/problem/3038

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def f(x: int, y: int, n: int):
    if y == (1 << n - 1):
        print(y*3-1-x)
        return
    print(x)
    f(x+y, y*2, n)
    f(x+y*2, y*2, n)


def solution(n: int):
    f(1, 1, n)


def main():
    n = read_single_int()
    solution(n)


if __name__ == '__main__':
    main()