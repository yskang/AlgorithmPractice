# Title: 별찍기 - 8
# Link: https://www.acmicpc.net/problem/2445

import sys

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(n: int):
    for i in range(n):
        print('*'*(i+1) + ' '*(n*2-2*(i+1)) + '*'*(i+1))
    for i in range(n-1, 0, -1):
        print('*'*i + ' '*(2*n-2*i) + '*'*i)

def main():
    N = read_single_int()
    solution(N)


if __name__ == '__main__':
    main()