# Title: A
# Link: https://www.acmicpc.net/problem/13171

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(a: int, x: int):
    return pow(a, x, 1000000007)


def main():
    a = read_single_int()
    x = read_single_int()
    print(solution(a, x))


if __name__ == '__main__':
    main()