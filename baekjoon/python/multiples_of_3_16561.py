# Title: 문제제목
# Link: https://www.acmicpc.net/problem/16561

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    seperator = n // 3 - 1
    return (seperator-1) * seperator // 2


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()