# Title: 꼬마 정민
# Link: https://www.acmicpc.net/problem/11382

import sys


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a: int, b: int, c: int) -> int:
    return a + b + c


def main():
    a, b, c = read_list_int()
    print(solution(a, b, c))


if __name__ == '__main__':
    main()