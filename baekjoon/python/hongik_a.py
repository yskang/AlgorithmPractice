# Title: 문제제목
# Link: https://www.acmicpc.net/problem/364/1

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(y: int):
    return y - 1946


def main():
    y = read_single_int()
    print(solution(y))


if __name__ == '__main__':
    main()