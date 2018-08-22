# Title: 타임머신
# Link: https://www.acmicpc.net/problem/11657
import collections
import sys

sys.setrecursionlimit(10 ** 6)

INF = 999999999999999


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


class Graph:
    def __init__(self):
        self.routes = []

    def add_route(self, start, end, time):
        self.routes.append((start, end, time))

    def get_route(self):
        return self.routes


def get_fastest_times(graph, N):
    times = [INF for _ in range(N+1)]
    times[1] = 0

    for _ in range(N-1):
        for (start, end, time) in graph.get_route():
            if times[start] + time < times[end]:
                times[end] = times[start] + time

    for (start, end, time) in graph.get_route():
        if times[start] + time < times[end]:
            return '-1'

    def make_str(n):
        return str(-1) if n == INF else str(n)

    return '\n'.join(map(make_str, times[2:]))


if __name__ == '__main__':
    N, M = read_list_int()
    graph = Graph()
    for _ in range(M):
        a, b, c = read_list_int()
        graph.add_route(a, b, c)
    print(get_fastest_times(graph, N))