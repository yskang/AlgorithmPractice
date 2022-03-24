# Title: 고려대학교에는 공식 와인이 있다
# Link: https://www.acmicpc.net/problem/16673

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(c: int, k: int, p: int):
    s = 0
    for i in range(1, c+1):
        s += k*i + p*(i**2)
    return s


def main():
    c, k, p = read_list_int()
    print(solution(c, k, p))


if __name__ == '__main__':
    main()