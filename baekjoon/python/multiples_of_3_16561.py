# Title: 문제제목
# Link: https://www.acmicpc.net/problem/16561

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def combination(n: int, r: int):
    if n == r or r == 0:
        return 1
    return combination(n-1, r-1) + combination(n-1, r)


def solution(n: int):
    num_threes = n // 3
    return combination(num_threes-1, 2)


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()