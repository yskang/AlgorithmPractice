# Title: 피보나치 수 6
# Link: https://www.acmicpc.net/problem/1144

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


MOD = 1000000007


def matrix_multiple(ma: list, mb: list):
    res = [[0 for _ in range(len(mb[0]))] for _ in range(len(ma))]
    for r, row in enumerate(ma):
        for c in range(len(mb[0])):
            for i, e in enumerate(row):
                res[r][c] += e * mb[i][c]
            res[r][c] %= MOD
    return res


def solution(n: int):
    bn = list(reversed(bin(n)[2:]))
    base = [[1, 1], [1, 0]]
    res = [[1, 0], [0, 1]]
    for x in bn:
        if x == '1':
            res = matrix_multiple(base, res)
        base = matrix_multiple(base, base)
    return res[0][1]


def main():
    print(solution(read_single_int()))


if __name__ == '__main__':
    main()