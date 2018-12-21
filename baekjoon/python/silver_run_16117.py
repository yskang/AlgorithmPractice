# Title: 실버런
# Link: https://www.acmicpc.net/problem/16117

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_silver_in(x: int, y: int, m: int, n: int, silver_map: list, dp: list):
    if not(0 <= x < m and 0 <= y < n):
        return 0
    if dp[y][x] != -1:
        return dp[y][x]
    if x == m-1 or x == 1:
        silver = max(get_silver_in(x-1, y-1, m, n, silver_map, dp), 
                    get_silver_in(x-1, y+1, m, n, silver_map, dp), 
                    get_silver_in(x-1, y, m, n, silver_map, dp), 
                    get_silver_in(x-2, y, m, n, silver_map, dp) + silver_map[y][x-1] if 0 <= x-1 < m else 0) + silver_map[y][x]
    else:
        silver =  max(get_silver_in(x-1, y-1, m, n, silver_map, dp), 
                    get_silver_in(x-1, y+1, m, n, silver_map, dp), 
                    get_silver_in(x-2, y, m, n, silver_map, dp) + silver_map[y][x-1] if 0 <= x-1 < m else 0) + silver_map[y][x]

    dp[y][x] = silver
    return silver


def get_silver_edge(x: int, y: int, m: int, n: int, silver_map: list, dp: list):
    if not(0 <= x <= m and 0 <= y <= n):
        return 0
    
    if dp[y][x] != -1:
        return dp[y][x]

    silver = max((get_silver_edge(x-1, y-1, m, n, silver_map, dp) + silver_map[y-1][x-1]) if 0 <= y-1 < n and 0 <= x-1 < m else 0,
                (get_silver_edge(x-1, y+1, m, n, silver_map, dp) + silver_map[y][x-1]) if 0 <= y < n and 0 <= x-1 < m else 0)

    dp[y][x] = silver
    return silver


def solution(n: int, m: int, silver_map: list):
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    dp_edge = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    max_silver_in = 0
    for i in range(n):
        max_silver_in = max(max_silver_in, get_silver_in(m-1, i, m, n, silver_map, dp))
    max_silver_edge = 0
    for i in range(n+1):
        max_silver_edge = max(max_silver_edge, get_silver_edge(m, i, m, n, silver_map, dp_edge))
    return max(max_silver_in, max_silver_edge)


def main():
    n, m = read_list_int()
    silver_map = []
    for _ in range(n):
        silver_map.append(read_list_int())
    print(solution(n, m, silver_map))


if __name__ == '__main__':
    main()