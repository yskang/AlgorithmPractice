# Title: KCM Travel
# Link: https://www.acmicpc.net/problem/10217

import sys

import collections
import heapq

sys.setrecursionlimit(10 ** 6)

INF = 9999999999999999


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


class Graph:
    def __init__(self, N):
        self.childs = [[] for _ in range(N + 1)]
        self.cost = collections.defaultdict(lambda: (INF, INF))

    def add_ticket(self, start, end, cost, time):
        self.childs[start].append(end)
        self.cost[(start, end)] = (cost, time)

    def get_next(self, node):
        return self.childs[node]

    def get_cost(self, start, end):
        return self.cost[(start, end)][0]

    def get_time(self, start, end):
        return self.cost[(start, end)][1]

    def get_total_cost(self, start, end):
        return self.cost[(start, end)]


def dijkstra(graph, start, M):
    # minimum_time[i][j] : minimum time to node i with cost j
    minimum_time = collections.defaultdict(lambda: INF)
    minimum_time[(1, 0)] = 0
    pq = []
    heapq.heappush(pq, (0, 0, start)) #(time, cost, node)
    min_time = INF
    while pq:
        time, cost, node = heapq.heappop(pq)

        if time > minimum_time[(node, cost)]:
            continue

        for child in graph.get_next(node):
            if cost + graph.get_cost(node, child) > M:
                continue
            new_time = minimum_time[(node, cost)] + graph.get_time(node, child)
            if new_time < minimum_time[(child, cost + graph.get_cost(node, child))]:
                minimum_time[(child, cost + graph.get_cost(node, child))] = new_time
                heapq.heappush(pq, (new_time, cost + graph.get_cost(node, child), child))
                if child == N:
                    min_time = min(min_time, new_time)

    return min_time


def get_minimum_time_to_LA(graph, N, M):
    min_time = dijkstra(graph, 1, M)
    # print(times)
    # print(times.keys())
    if min_time != INF:
        return min_time
    return 'Poor KCM'


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        N, M, K = read_list_int()
        graph = Graph(N)
        for _ in range(K):
            u, v, c, d = read_list_int()
            graph.add_ticket(u, v, c, d)
        print(get_minimum_time_to_LA(graph, N, M))
