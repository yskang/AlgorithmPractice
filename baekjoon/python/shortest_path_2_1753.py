# Title: 최단경로
# Link: https://www.acmicpc.net/problem/1753

import sys
from heapq import heappop, heappush
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


INF = 10**10


def dijkstra(start: int, child_of: defaultdict):
    hq = []
    distances = defaultdict(lambda: INF)
    distances[start] = 0
    heappush(hq, (0, start))

    while hq:
        dist, node = heappop(hq)

        if distances[node] < dist:
            continue

        for child, child_dist in child_of[node]:
            if dist+child_dist < distances[child]:
                distances[child] = dist+child_dist
                heappush(hq, (dist+child_dist, child))

    return distances


def solution(num_node: int, num_edge: int, start: int, child_of: defaultdict):
    dists = dijkstra(start, child_of)
    for i in range(1, num_node+1):
        if dists[i] != INF:
            print(dists[i])
        else:
            print('INF')


def main():
    v, e = read_list_int()
    s = read_single_int()
    child_of = defaultdict(lambda: [])
    for _ in range(e):
        a, b, w = read_list_int()
        child_of[a].append((b, w))
    solution(v, e, s, child_of)


if __name__ == '__main__':
    main()