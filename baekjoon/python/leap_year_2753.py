# Title: 윤년
# Link: https://www.acmicpc.net/problem/2753

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(y: int):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return 1
    return 0


def main():
    y = read_single_int()
    print(solution(y))


if __name__ == '__main__':
    main()