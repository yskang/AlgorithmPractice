# Title: 곱셈
# Link: https://www.acmicpc.net/problem/2588

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(a: int, b: int):
    b_str = str(b)
    for bn in reversed(b_str):
        print(a*int(bn))
    print(a*b)


def main():
    a = read_single_int()
    b = read_single_int()
    solution(a, b)


if __name__ == '__main__':
    main()