# Title: 별 찍기 - 17
# Link: https://www.acmicpc.net/problem/10992

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    print(' ' * (n-1) + '*')
    for i in range(2, n):
        print(' ' * (n-i) + '*' + ' '*(i*2-3) + '*' )
    if n != 1:
        print('*'*(n*2-1))


def main():
    N = read_single_int()
    solution(N)


if __name__ == '__main__':
    main()