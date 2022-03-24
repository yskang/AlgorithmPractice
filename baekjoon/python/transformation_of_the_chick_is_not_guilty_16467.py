# Title: 병아리의 변신은 무죄
# Link: https://www.acmicpc.net/problem/16467

import sys
import copy


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

MOD = 100000007

def multiple_matrix(n: int, a: list, b: list):
    res = []
    for row in a:
        t_row = []
        for i in range(n):
            s = 0
            for x, v in enumerate(row):
                s = (s + (v * (b[x][i] % MOD)) % MOD)%MOD
            t_row.append(s)
        res.append(t_row)
    return  res


def power_matrix(n: int, b: int, matrix: list):
    bin_b = list('{0:b}'.format(b))
    acc = [[1 if x==y else 0 for x in range(n)] for y in range(n)]
    temp = copy.deepcopy(matrix)
    if bin_b.pop() == '1':
        acc = multiple_matrix(n, acc, matrix)

    while bin_b:
        temp = multiple_matrix(n, temp, temp)
        if bin_b.pop() == '1':
            acc = multiple_matrix(n, acc, temp)
    
    return acc[0][0]


def solution(k, n):
    if k == 0:
        return pow(2, n, MOD)
    matrix = [[0 for _ in range(k+1)] for _ in range(k+1)]
    matrix[0][0] = 1
    matrix[0][k] = 1
    for i in range(k):
        matrix[i+1][i] = 1
    
    return power_matrix(k+1, n, matrix)


def main():
    t = read_single_int()
    for _ in range(t):
        k, n = read_list_int()
        print(solution(k, n))


if __name__ == '__main__':
    main()