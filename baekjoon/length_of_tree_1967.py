# Title: 트리의 지름
# Link: https://www.acmicpc.net/problem/1967

import sys

import collections

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


class Graph:
    def __init__(self):
        self.nodes = set()
        self.distances = {}
        self.neighbor = collections.defaultdict(lambda :[])

    def add_edge(self, f_node, t_node, distance):
        self.nodes.add(f_node)
        self.nodes.add(t_node)
        self.distances[(f_node, t_node)] = distance
        self.distances[(t_node, f_node)] = distance
        self.neighbor[f_node].append(t_node)
        self.neighbor[t_node].append(f_node)

    def get_neighbors(self, node):
        return self.neighbor[node]

    def get_distance(self, f_node, t_node):
        return self.distances[(f_node, t_node)]


def get_distance(graph, start, d, visited, max_distance):
    visited[start] = True
    if len(graph.get_neighbors(start)) == 1 and visited[graph.get_neighbors(start)[0]]:
        if d > max_distance[0]:
            max_distance[0] = d
            max_distance[1] = start
        return
    for to in graph.get_neighbors(start):
        if not visited[to]:
            get_distance(graph, to, d+graph.get_distance(start, to), visited, max_distance)


def get_max_distance(graph, start):
    max_distance = [0, 0]
    d = 0
    visited = [False for _ in range(n+1)]
    get_distance(graph, start, d, visited, max_distance)
    return max_distance[1], max_distance[0]


if __name__ == '__main__':
    n = read_single_int()
    graph = Graph()
    for _ in range(n-1):
        f_node, t_node, distance = read_list_int()
        graph.add_edge(f_node, t_node, distance)
    far_node, d = get_max_distance(graph, 1)
    far_node, d = get_max_distance(graph, far_node)
    print(d)