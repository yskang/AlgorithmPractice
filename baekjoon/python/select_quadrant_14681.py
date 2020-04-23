# Title: 사분면 고르기
# Link: https://www.acmicpc.net/problem/14681

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(x: int, y: int):
    if 0 < x:
        return 1 if y > 0 else 4
    else:
        return 2 if y > 0 else 3


def main():
    x = read_single_int()
    y = read_single_int()
    print(solution(x, y))


if __name__ == '__main__':
    main()