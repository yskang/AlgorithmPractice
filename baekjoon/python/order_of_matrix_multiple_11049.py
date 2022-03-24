# Title: 행렬 곱셈 순서
# Link: https://www.acmicpc.net/problem/11049

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_min_times(start: int, end: int, matrixs: list, dp: list):
    if dp[start][end] != -1:
        return dp[start][end]

    if end == start:
        dp[start][end] = 0
        return 0

    min_value = 999999999999999999999
    for i in range(start, end):
        min_value = min(get_min_times(start, i, matrixs, dp) + get_min_times(i+1, end, matrixs, dp) + (matrixs[start][0] * matrixs[end][1] * matrixs[i][1]), min_value)
    
    dp[start][end] = min_value
    return min_value


def solution(n: int, matrixs: list):
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    return get_min_times(1, n, matrixs, dp)


def main():
    n = read_single_int()
    matrixs = [0]
    for _ in range(n):
        matrixs.append(read_list_int())
    print(solution(n, matrixs))


if __name__ == '__main__':
    main()