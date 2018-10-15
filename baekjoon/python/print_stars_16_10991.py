# Title: 별 찍기 - 16
# Link: https://www.acmicpc.net/problem/10991

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(n: int):
    for i in range(1, n+1):
        print(' ' * (n-i) +' '.join(['*' for _ in range(i)]))


def main():
    N = read_single_int()
    solution(N)


if __name__ == '__main__':
    main()