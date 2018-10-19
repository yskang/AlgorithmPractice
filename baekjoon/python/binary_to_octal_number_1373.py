# Title: 2진수 8진수
# Link: https://www.acmicpc.net/problem/1373

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def solution(b: str):
    return oct(int(b, 2))[2:]


def main():
    b = read_single_str()
    print(solution(b))


if __name__ == '__main__':
    main()