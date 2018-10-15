# Title: 별찍기 - 9
# Link: https://www.acmicpc.net/problem/2446

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(n: int):
    for i in range(n):
        print(' '*(i)+'*'*(2*n-1-2*i))
    for i in range(n-2, -1, -1):
        print(' '*(i)+'*'*(2*n-1-2*i))

def main():
    N = read_single_int()
    solution(N)


if __name__ == '__main__':
    main()