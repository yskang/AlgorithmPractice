# Title: 곰곰이의 심부름
# Link: https://www.acmicpc.net/problem/25198

import sys
from collections import defaultdict
from math import comb
from heapq import heappush, heappop


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


INF = pow(10, 10)-1


def dijkstra(graph: defaultdict, start: int, n: int):
    pq = []
    times = [INF for _ in range(n+1)]
    befores = [None for _ in range(n+1)]

    times[start] = 0
    heappush(pq, (0, start))

    while pq:
        time, node = heappop(pq)
        if time != times[node]:
            continue
        for next_node in graph[node]:
            new_time = 1 + time
            if new_time < times[next_node]:
                times[next_node] = new_time
                befores[next_node] = node
                heappush(pq, (new_time, next_node))

    return times, befores


def solution(n: int, s: int, c: int, h: int, g: defaultdict):
    times_sc, befores_sc = dijkstra(g, s, n)
    times_hc, befores_hc = dijkstra(g, h, n)

    current = c
    duplications = 0

    while True:
        if befores_sc[current] == befores_hc[current]:
            current = befores_sc[current]
            if not current:
                break
            duplications += 1
        else:
            break

    return comb(times_sc[c] + times_hc[c] + 1 - duplications, 2) + comb(duplications + 1, 2)


def main():
    n = read_single_int()
    s, c, h = read_list_int()
    g = defaultdict(lambda: [])
    for _ in range(n-1):
        u, v = read_list_int()
        g[u].append(v)
        g[v].append(u)
    print(solution(n, s, c, h, g))


if __name__ == '__main__':
    main()