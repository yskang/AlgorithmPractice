# Title: 알람 시계
# Link: https://www.acmicpc.net/problem/2882

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(h: int, m: int):
    if m >= 45:
        return [h, m-45]
    if h == 0:
        return [23, 15+m]
    return [h-1, 15+m]


def main():
    h, m = read_list_int()
    print(*solution(h, m))


if __name__ == '__main__':
    main()