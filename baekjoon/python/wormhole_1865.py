# Title: 웜홀
# Link: https://www.acmicpc.net/problem/1865

import sys

import collections

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


INF = 99999999999999999


class Graph:
    def __init__(self):
        self.edges = []

    def add_road(self, start, end, cost):
        self.edges.append((start, end, cost))
        self.edges.append((end, start, cost))

    def add_wormhole(self, start, end, cost):
        self.edges.append((start, end, -cost))


def bellman_ford(graph, start, N):
    dist = collections.defaultdict(lambda: INF)
    dist[start] = 0

    for i in range(1, N):
        for (s, e, cost) in graph.edges:
            if dist[s] + cost < dist[e]:
                dist[e] = dist[s] + cost

    for (s, e, cost) in graph.edges:
        if dist[s] + cost < dist[e]:
            return 'YES'

    return 'NO'


def varify_path(graph, N):
    return bellman_ford(graph, 1, N)


if __name__ == '__main__':
    Te = read_single_int()
    for _ in range(Te):
        graph = Graph()
        N, M, W = read_list_int()
        for _ in range(M):
            S, E, T = read_list_int()
            graph.add_road(S, E, T)
        for _ in range(W):
            S, E, T = read_list_int()
            graph.add_wormhole(S, E, T)
        print(varify_path(graph, N))