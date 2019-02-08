# Title: 행렬 제곱
# Link: https://www.acmicpc.net/problem/10830

import sys
import copy

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def multiple_matrix(n: int, a: list, b: list):
    res = []
    for row in a:
        t_row = []
        for i in range(n):
            s = 0
            for x, v in enumerate(row):
                s = (s + (v * (b[x][i] % 1000)) % 1000)%1000
            t_row.append(s)
        res.append(t_row)
    return  res


def solution(n: int, b: int, matrix: list):
    bin_b = list('{0:b}'.format(b))
    acc = [[1 if x==y else 0 for x in range(n)] for y in range(n)]
    temp = copy.deepcopy(matrix)
    if bin_b.pop() == '1':
        acc = multiple_matrix(n, acc, matrix)

    while bin_b:
        temp = multiple_matrix(n, temp, temp)
        if bin_b.pop() == '1':
            acc = multiple_matrix(n, acc, temp)
    
    temp = [[1 if x==y else 0 for x in range(n)] for y in range(n)]

    ans = []
    for row in acc:
        ans.append(' '.join(map(str, row)))
    return '\n'.join(ans)
    

def main():
    n, b = read_list_int()
    matrix = []
    for _ in range(n):
        matrix.append(read_list_int())
    print(solution(n, b, matrix))


if __name__ == '__main__':
    main()