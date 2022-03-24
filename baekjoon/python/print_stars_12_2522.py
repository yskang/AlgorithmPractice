# Title: 별찍기 - 12
# Link: https://www.acmicpc.net/problem/2522

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(n: int):
    for i in range(n-1, -1, -1):
        print(' ' * i + '*' * (n - i))
    for i in range(1, n):
        print(' ' * i + '*' * (n-i))


def main():
    N = read_single_int()
    solution(N)


if __name__ == '__main__':
    main()