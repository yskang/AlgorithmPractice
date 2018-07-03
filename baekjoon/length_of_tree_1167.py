# Title: 트리의 지금
# Link: https://www.acmicpc.net/problem/1167

import sys

import heapq

from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


class Graph():
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.costs = {}

    def neighbors(self, n):
        return self.edges[n]

    def get_cost(self, f, t):
        return self.costs[(f, t)]

    def get_list_nodes(self):
        return list(self.nodes)

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, cost):
        self._add_edge(from_node, to_node, cost)
        # self._add_edge(to_node, from_node, cost)

    def _add_edge(self, from_node, to_node, cost):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.costs[(from_node, to_node)] = cost


def parse(l, graph):
    graph.add_node(l[0])
    nodes = l[1:-2]
    for i in range(0, len(nodes), 2):
        graph.add_edge(nodes[i], l[0], nodes[i+1])


def Dijkstra(graph, start):
    costs = defaultdict(lambda: 99999999999)
    prev = {}
    pq = []
    costs[start] = 0
    prev[start] = None

    heapq.heappush(pq, (costs[start], start))

    while len(pq) > 0:
        p, u = heapq.heappop(pq)
        for v in graph.neighbors(u):
            alt = costs[u] + graph.get_cost(u, v)
            if alt < costs[v]:
                costs[v] = alt
                prev[v] = u
                heapq.heappush(pq, (costs[v], v))

    return sorted(costs.items(), key=lambda item: item[1], reverse=True)[0]


if __name__ == '__main__':
    V = read_single_int()
    graph = Graph()
    edge_nodes = []
    for _ in range(V):
        l = read_list_int()
        graph.add_node(l[0])
        nodes = l[1:-1]
        if len(nodes) == 2:
            edge_nodes.append(l[0])
        for i in range(0, len(nodes), 2):
            graph.add_edge(l[0], nodes[i], nodes[i+1])
    (far_node, dist) = Dijkstra(graph, 1)
    (_, max_dist) = Dijkstra(graph, far_node)
    print(max_dist)