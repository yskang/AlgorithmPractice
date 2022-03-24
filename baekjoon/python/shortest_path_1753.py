# Title: 최단경로
# Link: https://www.acmicpc.net/problem/1753

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
    def __init__(self):
        self.child_of = collections.defaultdict(lambda: set())
        self.costs_of = collections.defaultdict(lambda: INF)

    def add_edge(self, start, end, weight):
        self.child_of[start].add(end)
        self.costs_of[(start, end)] = min(weight, self.costs_of[(start, end)])

    def get_child_of(self, node):
        return self.child_of[node]

    def get_cost(self, start, end):
        return self.costs_of[(start, end)]


def dijkstra(graph, start, V):
    dist = collections.defaultdict(lambda: INF)
    pq = []

    dist[start] = 0

    heapq.heappush(pq, (dist[start], start))

    while pq:
        distance, node = heapq.heappop(pq)
        for child in graph.get_child_of(node):
            new_distance = dist[node] + graph.get_cost(node, child)
            if new_distance < dist[child]:
                dist[child] = new_distance
                heapq.heappush(pq, (dist[child], child))

    ans = []
    for i in range(1, V+1):
        ans.append('INF') if dist[i] == INF else ans.append(str(dist[i]))

    return '\n'.join(ans)


if __name__ == '__main__':
    V, E = read_list_int()
    K = read_single_int()
    graph = Graph()
    for _ in range(E):
        u, v, w = read_list_int()
        graph.add_edge(u, v, w)
    print(dijkstra(graph, K, V))