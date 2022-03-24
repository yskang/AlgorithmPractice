# Title: A+B - 7
# Link: https://www.acmicpc.net/problem/11021

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def solution(a: int, b: int):
    return a+b


def main():
    T = read_single_int()
    for i in range(1, T+1):
        A, B = read_list_int()
        print('Case #{}: {}'.format(i, solution(A, B)))


if __name__ == '__main__':
    main()