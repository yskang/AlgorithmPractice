# Title: 두 수 비교하기
# Link: https://www.acmicpc.net/problem/1330

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a: int, b: int):
    if a < b:
        return '<'
    elif a > b:
        return '>'
    return '=='


def main():
    a, b = read_list_int()
    print(solution(a, b))


if __name__ == '__main__':
    main()