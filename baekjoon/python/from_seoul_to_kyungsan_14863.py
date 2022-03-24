# Title: 서울에서 경산까지
# Link: https://www.acmicpc.net/problem/14863

import sys
from types import SimpleNamespace

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def solution(n: int, k: int, gets: list):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(k+1):
        dp[1][i] = max(0 if (gets[1].walk.time > i) else gets[1].walk.money, 0 if (gets[1].bike.time > i) else gets[1].bike.money)
    
    for i in range(2, n+1):
        for j in range(1, k+1):
            a, b = 0, 0
            if gets[i].walk.time <= j and dp[i-1][j-gets[i].walk.time] != 0:
                a = dp[i-1][j-gets[i].walk.time] + gets[i].walk.money
            if gets[i].bike.time <= j and dp[i-1][j-gets[i].bike.time] != 0:
                b = dp[i-1][j-gets[i].bike.time] + gets[i].bike.money
            dp[i][j] = max(a, b)
    return dp[n][k]


def main():
    n, k = read_list_int()
    gets = [()]
    for _ in range(n):
        w_t, w_m, b_t, b_m = read_list_int()
        gets.append(SimpleNamespace(walk=SimpleNamespace(time= w_t, money= w_m), bike=SimpleNamespace(time= b_t, money= b_m)))
    print(solution(n, k, gets))


if __name__ == '__main__':
    main()