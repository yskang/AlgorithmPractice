# Title: 평범한 배낭
# Link: https://www.acmicpc.net/problem/12865

import sys
from types import SimpleNamespace

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, k: int, items: list):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for item_number, item in enumerate(items, 1):
        for weigth_limit in range(k+1):
            dp[item_number][weigth_limit] = max(dp[item_number-1][weigth_limit], 
                                    (item.value + dp[item_number-1][weigth_limit-item.weight]) if weigth_limit-item.weight >= 0 else 0)

    return dp[n][k]
    

def main():
    n, k = read_list_int()
    wvs = []
    for _ in range(n):
        w, v = read_list_int()
        wvs.append(SimpleNamespace(weight= w, value= v))
    print(solution(n, k, wvs))


if __name__ == '__main__':
    main()