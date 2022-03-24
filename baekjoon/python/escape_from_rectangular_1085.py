# Title: 직사각형에서 탈출
# Link: https://www.acmicpc.net/problem/1085

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(x, y, w, h):
    return min(h-y, x, y, w-x)


def main():
    x, y, w, h = read_list_int()
    print(solution(x, y, w, h))


if __name__ == '__main__':
    main()