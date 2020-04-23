# Title: 별 찍기 21
# Link: https://www.acmicpc.net/problem/10996

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    for _ in range(n):
        line = ('* ' * (1 + n//2))[0:n]
        print(line)
        if n != 1:
            print(' ' + line[:-1])


def main():
    n = read_single_int()
    solution(n)


if __name__ == '__main__':
    main()