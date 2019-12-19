# Title: 피보나치 수 5
# Link: https://www.acmicpc.net/problem/10870

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def get_fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return get_fibonacci(n-1) + get_fibonacci(n-2)


def solution(n: int):
    return get_fibonacci(n)


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()