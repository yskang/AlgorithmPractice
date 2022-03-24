# Title: 별 찍기 13
# Link: https://www.acmicpc.net/problem/2523

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    for i in range(n):
        print('*'*(i+1))
    for i in range(n-1, 0, -1):
        print('*'*i)


def main():
    n = read_single_int()
    solution(n)


if __name__ == '__main__':
    main()