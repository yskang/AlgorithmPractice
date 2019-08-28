# Title: 운동
# Link: https://www.acmicpc.net/problem/1956

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
INF = 10**10


def solution(v: int, e: int, dist: list):
    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
    min_cycle = INF
    for i in range(1, v+1):
        min_cycle = min(min_cycle, dist[i][i])
    return -1 if min_cycle == INF else min_cycle


def main():
    v, e = read_list_int()
    dist = [[INF for _ in range(v+1)] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = read_list_int()
        dist[a][b] = c
    print(solution(v, e, dist))


if __name__ == '__main__':
    main()