# Title: 격자판 채우기
# Link: https://www.acmicpc.net/problem/1648

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_count(idx: int, status: int, dp: list, n: int, m: int):
    if idx == n*m:
        return 1 if status == 0 else 0
    if idx > n*m:
        return 0
    if dp[idx][status] != -1:
        return dp[idx][status]
    
    if status & 1:
        dp[idx][status] = get_count(idx+1, status >> 1, dp, n, m)
    else:
        dp[idx][status] = get_count(idx+1, (status>>1) | (1<<(m-1)), dp, n, m)
        if (idx+1) % m != 0 and status & 2 == 0:
            dp[idx][status] += get_count(idx+2, status>>2, dp, n, m)
    return dp[idx][status]


def solution(n: int, m: int):
    dp = [[-1 for _ in range(1<<m)] for _ in range(n*m)]
    return get_count(0, 0, dp, n, m) % 9901


def main():
    n, m = read_list_int()
    print(solution(n, m))


if __name__ == '__main__':
    main()