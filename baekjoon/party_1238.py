# Title: 파티
# Link: https://www.acmicpc.net/problem/1238
import collections
import heapq
import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


INF = 9999999999999999


class Graph:
    def __init__(self, num_node):
        self.nodes = [[] for _ in range(num_node+1)]

    def add_road(self, start, end, time):
        self.nodes[start].append((end, time))

    def get_next_of(self, node):
        return self.nodes[node]


def dijkstra(graph, start):
    pq = []
    times = collections.defaultdict(lambda: INF)
    times[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        time, node = heapq.heappop(pq)
        if time != times[node]:
            continue
        for next_node, add_time in graph.get_next_of(node):
            new_time = add_time + time
            if new_time < times[next_node]:
                times[next_node] = new_time
                heapq.heappush(pq, (new_time, next_node))
    return times


def get_max_move_time(graph, num_node, party_node):
    max_time = 0
    way_homes = dijkstra(graph, party_node)
    way_party = dijkstra(graph_reverse, party_node)

    for node in range(1, num_node+1):
        max_time = max(way_party[node] + way_homes[node], max_time)
    return max_time


if __name__ == '__main__':
    N, M, X = read_list_int()
    graph = Graph(N)
    graph_reverse = Graph(N)
    for _ in range(M):
        start, end, time = read_list_int()
        graph.add_road(start, end, time)
        graph_reverse.add_road(end, start, time)
    print(get_max_move_time(graph, N, X))