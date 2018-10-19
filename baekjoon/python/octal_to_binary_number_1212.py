# Title: 8진수 2진수
# Link: https://www.acmicpc.net/problem/1212

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def solution(o: str):
    return bin(int(o, 8))[2:]


def main():
    o = read_single_str()
    print(solution(o))


if __name__ == '__main__':
    main()