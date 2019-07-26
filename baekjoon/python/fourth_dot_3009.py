# Title: 네 번째 점
# Link: https://www.acmicpc.net/problem/3009

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(xys: list):
    a, b = 0, 0
    for x, y in xys:
        a ^= x
        b ^= y
    return (a, b)

def main():
    xys = []
    for _ in range(3):
        xys.append(read_list_int())
    print(*solution(xys))


if __name__ == '__main__':
    main()