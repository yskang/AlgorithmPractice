# Title: 특정한 최단 경로
# Link: https://www.acmicpc.net/problem/1504

import sys

import collections
import heapq

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


INF = 999999999999999999


class Graph:
    def __init__(self):
        self.child_of = collections.defaultdict(lambda: set())
        self.distance_of = collections.defaultdict(lambda: INF)

    def add_edge(self, start, end, distance):
        self.child_of[start].add(end)
        self.child_of[end].add(start)
        self.distance_of[(start, end)] = distance
        self.distance_of[(end, start)] = distance

    def get_distance_of(self, start, end):
        return self.distance_of[(start, end)]

    def get_child_of(self, node):
        return self.child_of[node]


def dijkstra(graph, start):
    dist = collections.defaultdict(lambda: INF)
    pq = []

    dist[start] = 0

    heapq.heappush(pq, (dist[start], start))

    while pq:
        distance, node = heapq.heappop(pq)
        for child in graph.get_child_of(node):
            new_distance = graph.get_distance_of(node, child) + distance
            if new_distance < dist[child]:
                dist[child] = new_distance
                heapq.heappush(pq, (new_distance, child))

    return dist


def get_shortest_length_of_special_path(graph, s1, s2, N):
    middle = dijkstra(graph, s1)[s2]
    if middle == INF:
        return -1
    dist = dijkstra(graph, 1)
    one_to_s1 = dist[s1]
    one_to_s2 = dist[s2]
    dist = dijkstra(graph, N)
    N_to_s1 = dist[s1]
    N_to_s2 = dist[s2]
    min_sides = min(one_to_s1 + N_to_s2, one_to_s2 + N_to_s1)
    if min_sides > INF:
        return -1
    return  min_sides + middle


if __name__ == '__main__':
    N, E = read_list_int()
    graph = Graph()
    for _ in range(E):
        a, b, c = read_list_int()
        graph.add_edge(a, b, c)
    s1, s2 = read_list_int()
    print(get_shortest_length_of_special_path(graph, s1, s2, N))