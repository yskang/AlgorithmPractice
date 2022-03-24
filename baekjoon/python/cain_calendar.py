# https://www.acmicpc.net/problem/6064
import sys


def get_cain_calendar(M, N, x, y):
    if N == min(M, N):
        M, N = N, M
        x, y = y, x

    for m in range(40001):
        if (M * m + x - y) % N == 0:
            n = (M * m + x - y) / N
            if (N * n + y - x) % M == 0:
                return int(N * n + y)

    return -1


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        [M, N, x, y] = list(map(int, sys.stdin.readline().strip().split()))
        print(get_cain_calendar(M, N, x, y))