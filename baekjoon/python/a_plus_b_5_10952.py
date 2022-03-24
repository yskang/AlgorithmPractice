# Title: A+B - 5
# Link: https://www.acmicpc.net/problem/10952

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def solution(a: int, b: int):
    return a+b


def main():
    while True:
        A, B = read_list_int()
        ans = solution(A, B)
        if ans == 0:
            break
        print(ans)


if __name__ == '__main__':
    main()