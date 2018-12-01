# Title: 파스칼의 삼각형
# Link: https://www.acmicpc.net/problem/364/2

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, k: int):
    row = [1]
    row_2 = []
    while n > 1:
        row.append(0)
        prev = 0
        for r in row:
            row_2.append(prev+r)
            prev = r
        row = row_2[:]
        row_2 = []
        n-=1
    return row[k-1]


def main():
    n, k = read_list_int()
    print(solution(n, k))


if __name__ == '__main__':
    main()