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


def check_reach(graph, N, M):
    pq = []
    costs = collections.defaultdict(lambda: INF)
    prev = collections.defaultdict(lambda: 0)
    costs[1] = 0
    prev[1] = (0, 0)
    heapq.heappush(pq, (0, 1))

    while pq:
        cost, node = heapq.heappop(pq)

        if cost != costs[node]:
            continue

        for next_node, cost_next, time_next in graph.get_next(node):
            new_cost = cost + cost_next
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                prev[next_node] = (node, time_next)
                heapq.heappush(pq, (new_cost, next_node))

    time_sum = 0
    if costs[N] <= M:
        n = N
        while True:
            (n, t) = prev[n]
            time_sum += t
            if n == 0:
                break
        return False, time_sum
    return True, time_sum


def dijkstra(graph, start, M, time_limit):
    # minimum_time = [[INF] * (M+1) for _ in range(N+1)]
    minimum_time = collections.defaultdict(lambda: collections.defaultdict(lambda: INF))
    minimum_time[1][0] = 0
    pq = []
    heapq.heappush(pq, (0, 0, start)) #(time, cost, node)
    min_time = INF

    while pq:
        time, cost, node = heapq.heappop(pq)

        if min_time <= time:
            continue

        if minimum_time[node][cost] < time:
            continue

        for child, cost_c, time_c in graph.get_next(node):
            cost_node_to_child = cost + cost_c
            if cost_node_to_child > M:
                continue
            new_time = minimum_time[node][cost] + time_c

            if new_time > time_limit:
                continue

            if min_time <= new_time:
                continue

            if child == N:
                min_time = new_time
                continue

            if new_time < minimum_time[child][cost_node_to_child]:
                minimum_time[child][cost_node_to_child] = new_time
                heapq.heappush(pq, (new_time, cost_node_to_child, child))

    return min_time


def get_minimum_time_to_LA(graph, N, M):
    # min_time = solve(graph, N, M)
    is_poor_kcm, time = check_reach(graph, N, M)
    if is_poor_kcm:
        return 'Poor KCM'
    # return solve(graph, N, M)
    return dijkstra(graph, 1, M, time)


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        N, M, K = read_list_int()
        graph = Graph(N)
        for _ in range(K):
            u, v, c, d = read_list_int()
            graph.add_ticket(u, v, c, d)
        print(get_minimum_time_to_LA(graph, N, M))
