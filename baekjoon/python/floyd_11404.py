# Title: 플로이드
# Link: https://www.acmicpc.net/problem/11404

import sys
from collections import defaultdict
from heapq import heappush, heappop


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

INF = 10 ** 10

def solution(n: int, m: int, bus: list):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if bus[i][j] > bus[i][k] + bus[k][j]:
                    bus[i][j] = bus[i][k] + bus[k][j]
    
    for row in bus[1:]:
        row = list(map(lambda x: 0 if x == INF else x, row))
        print(*row[1:])


def main():
    n = read_single_int()
    m = read_single_int()
    bus = [[0 if i==j else INF for i in range(n+1)] for j in range(n+1)]
    for _ in range(m):
        a, b, c = read_list_int()
        bus[a][b] = min(bus[a][b], c)
    solution(n, m, bus)


if __name__ == '__main__':
    main()