# Title: 방 배정하기
# Link: https://www.acmicpc.net/problem/14697

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a: int, b: int, c: int, n: int):
    for x in range(51):
        for y in range(51):
            for z in range(51):
                if x*a + y*b + z*c == n:
                    return 1
    return 0


def main():
    a, b, c, n = read_list_int()
    print(solution(a, b, c, n))


if __name__ == '__main__':
    main()