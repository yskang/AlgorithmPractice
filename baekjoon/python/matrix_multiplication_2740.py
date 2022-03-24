# Title: 행렬의 곱셈
# Link: https://www.acmicpc.net/problem/2740

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_miltiplication_matrix(a, b):
    res = []
    for j, row_a in enumerate(a):
        row = []
        for k in range(len(b[0])):
            elem = 0
            for i, elem_a in enumerate(row_a):
                elem += elem_a * b[i][k]
            row.append(elem)
        res.append(row)
    return res


if __name__ == '__main__':
    N, M = read_list_int()
    A = []
    for _ in range(N):
        A.append(read_list_int())
    M, K = read_list_int()
    B = []
    for _ in range(M):
        B.append(read_list_int())
    for row in get_miltiplication_matrix(A, B):
        print(' '.join(map(str, row)))
