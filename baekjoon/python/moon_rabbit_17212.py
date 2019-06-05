# Title: 달라라 토끼를 위한 구매대금 지불 도우미
# Link: https://www.acmicpc.net/problem/17212

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    r = n % 7
    d = n//7
    if r == 0:
        return d
    elif r == 1:
        return d + 1
    elif r == 2:
        return d + 1
    elif d == 0 and r == 3:
        return d + 2
    elif d != 0 and r == 3:
        return d + 1
    elif r == 4:
        return d + 2
    elif r == 5:
        return d + 1
    elif r == 6:
        return d + 2


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()