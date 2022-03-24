# Title: 당근 훔쳐 먹기
# Link: https://www.acmicpc.net/problem/18234

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, t: int, carrots: list):
    max_tates = 0

    for i, [w, p] in enumerate(carrots):
        carrots[i] = [w+p*(t-n), p]

    carrots = sorted(carrots, key=lambda x: x[1])
    for d, [w, p] in enumerate(carrots):
        max_tates += (w+d*p)

    return max_tates


def main():
    n, t = read_list_int()
    carrots = []
    for _ in range(n):
        carrots.append(read_list_int())
    print(solution(n, t, carrots))


if __name__ == '__main__':
    main()