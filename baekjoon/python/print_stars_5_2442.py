# Title: 별찍기 - 5
# Link: https://www.acmicpc.net/problem/2442

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(n: int):
    for i in range(n):
        print(' ' * (n - 1 - i) + '*'* (i*2+1))


def main():
    N = read_single_int()
    solution(N)


if __name__ == '__main__':
    main()