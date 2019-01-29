# Title: 영화감독 숌
# Link: https://www.acmicpc.net/problem/1436

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    x = 0
    while n > 0:
        x += 1
        if str(x).find('666') != -1:
            n -= 1
    return x


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()