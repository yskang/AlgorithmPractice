# Title: KCM Travel
# Link: https://www.acmicpc.net/problem/10217

import sys

import collections
import heapq

sys.setrecursionlimit(10 ** 6)

INF = 100*1000+1


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


class Graph:
    def __init__(self, N):
        self.childs = [[] for _ in range(N+1)]

    def add_ticket(self, start, end, cost, time):
        self.childs[start].append((end,cost,time))

    def get_next(self, node):
        return self.childs[node]


def solve(graph, N, M):
    times = [[INF]*(M+1) for _ in range(N+1)]
    times[1][0] = 0
    for cost in range(M):
        for current in range(1, N):
            if times[current][cost] == INF:
                continue
            for child, cost_child, time_child in graph.get_next(current):
                new_cost = cost + cost_child
                if new_cost > M:
                    continue
                new_time = times[current][cost] + time_child
                if new_time < times[child][new_cost]:
                    times[child][new_cost] = new_time
    return min(times[N])


def get_minimum_time_to_LA(graph, N, M):
    min_time = solve(graph, N, M)
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
