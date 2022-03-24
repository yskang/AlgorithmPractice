# Title: 화살표 연산자
# Link: https://www.acmicpc.net/problem/16114

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(x: int, n: int):
    if n == 0 and x > 0:
        return 'INFINITE'
    elif n == 0:
        return 0
    if n == 1 and x < 0:
        return 'INFINITE'
    elif n == 1:
        return 0
    if n % 2 == 1:
        return 'ERROR'
    if x <= 0:
        return 0
    n = n // 2
    return (x // n) - 1 if x%n == 0 else x//n



def main():
    x, n = read_list_int()
    print(solution(x, n))


if __name__ == '__main__':
    main()