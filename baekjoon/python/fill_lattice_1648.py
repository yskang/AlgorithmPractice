# Title: 격자판 채우기
# Link: https://www.acmicpc.net/problem/1648

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_count(curr: int, mask: int, dp: list, n: int, m: int):
    if curr > n*m:
        return 0
    if curr == n*m:
        return 1 if mask == 0 else 0
    if dp[curr][mask] != -1:
        return dp[curr][mask]

    if mask & 1:
        dp[curr][mask] = get_count(curr+1, mask>>1, dp, n, m)
    else:
        dp[curr][mask] = get_count(curr+1, (mask>>1)|(1<<(m-1)), dp, n, m)
        if curr % m != (m-1) and (mask & 1<<1) == 0:
            dp[curr][mask] += get_count(curr+2, (mask>>2), dp, n, m)
    return dp[curr][mask]


def solution(n: int, m: int):
    dp = [[-1 for i in range(1<<14)] for j in range(n*m)]
    return get_count(0, 0, dp, n, m) % 9901


def main():
    n, m = read_list_int()
    print(solution(n, m))


if __name__ == '__main__':
    main()