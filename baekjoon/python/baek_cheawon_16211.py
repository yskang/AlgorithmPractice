# Title: 백채원
# Link: https://www.acmicpc.net/problem/16211

import sys
import collections
import heapq


sys.setrecursionlimit(10 ** 6)

INF = 999999999999999

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class Graph:
    def __init__(self, n):
        self.childs = [[] for _ in range(n+1)]

    def add_road(self, a, b, t):
        self.childs[a].append([b, t])
        self.childs[b].append([a, t])


def dijkstra(g: Graph, ss: list):
    costs = collections.defaultdict(lambda: INF)
    pq = []
    for s in ss:
        heapq.heappush(pq, (0, s))
        costs[s] = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if costs[node] != cost:
            continue

        for (child, c) in g.childs[node]:
            if cost+c < costs[child]:
                costs[child] = cost+c
                heapq.heappush(pq, (cost+c, child))

    return costs


def solution(n: int, m: int, k: int, graph: Graph, ks: list):
    bcw = dijkstra(graph, [1])
    fans = dijkstra(graph, ks)

    is_ans = False
    for i in range(2, n+1):
        if bcw[i] < fans[i]:
            is_ans = True
            print(i, end=' ')

    if not is_ans:
        print(0)


def main():
    n, m, k = read_list_int()
    grpah = Graph(n)
    for _ in range(m):
        a, b, t = read_list_int()
        grpah.add_road(a, b, t)
    ks = read_list_int()
    solution(n, m, k, grpah, ks)


if __name__ == '__main__':
    main()