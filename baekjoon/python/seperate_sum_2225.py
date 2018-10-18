# Title: 합분해
# Link: https://www.acmicpc.net/problem/2225

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, k: int):
    d = [[0 for _ in range(n+1)], [1 for _ in range(n+1)]] + [[0 for _ in range(n+1)] for _ in range(k-1)]

    for y in range(2, k+1):
        for x in range(n+1):
            d[y][x] = sum(d[y-1][:x+1])

    return d[k][n] % 1000000000


def main():
    N, K = read_list_int()
    print(solution(N, K))


if __name__ == '__main__':
    main()