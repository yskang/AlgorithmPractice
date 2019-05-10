# Title: 열혈강호2
# Link: https://www.acmicpc.net/problem/11376

import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 6)


def read_list_int(): return list(map(int, sys.stdin.readline().strip().split(' ')))


def make_source_to_first_group_as_childs(g: defaultdict, source: int, group_start: int, group_end: int):
    for n in range(group_start, group_end+1):
        g[source][n] = min(len(g[n].keys()), 2)
        g[n][source] = 0


def make_second_group_to_sink(g: defaultdict, sink: int, group_start: int, group_end: int):
    for n in range(group_start, group_end+1):
        g[n][sink] = 1
        g[sink][n] = 0


def add_connections(g: defaultdict, node_from: int, node_to: int):
    g[node_from][node_to] = 1
    g[node_to][node_from] = 0


class Dinic:
    def __init__(self, source: int, sink: int):
        self.g = defaultdict(lambda: defaultdict(lambda: 0))
        self.source = source
        self.sink = sink
        self.total_flow = 0

    def bfs(self, level_of: list):
        queue = deque()
        queue.append(self.source)

        while queue:
            node = queue.popleft()
            level = level_of[node]

            for child in self.g[node].keys():
                if level_of[child] == -1 and self.g[node][child] > 0:
                    level_of[child] = level+1
                    queue.append(child)

    def dfs(self, level_of: list, node: int, visited: defaultdict, paths: list):
        if visited[node]:
            return
        visited[node] = True
        paths.append(node)

        for child in self.g[node].keys():
            if level_of[child] - level_of[node] == 1 and self.g[node][child] > 0:
                self.dfs(level_of, child, visited, paths)

        if node == self.sink:
            visited[node] = False
            min_capa = pow(10, 10)
            s = self.source
            for node in paths[1:]:
                if self.g[s][node] < min_capa:
                    min_capa = self.g[s][node]
                s = node
            self.total_flow += min_capa
            s = self.source
            for node in paths[1:]:
                self.g[s][node] -= min_capa
                self.g[node][s] += min_capa
                s = node

        paths.pop()

    def get_maximum_flow(self):
        while True:
            level_of = [-1 for _ in range(len(self.g)+5)]
            level_of[self.source] = 0
            self.bfs(level_of)
            if level_of[self.sink] == -1:
                break
            visited = defaultdict(lambda: False)
            paths = []
            self.dfs(level_of, self.source, visited, paths)
        return self.total_flow


def print_graph(g: defaultdict):
    for k in g:
        print('{} - [{}]'.format(k, g[k]))


def solution(dinic: Dinic):
    return dinic.get_maximum_flow()


def main():
    n, m = read_list_int()

    dinic = Dinic(0, n+m+1)

    for e in range(1, n+1):
        works = read_list_int()
        for work in works[1:]:
            add_connections(dinic.g, e, work+n)

    make_source_to_first_group_as_childs(dinic.g, 0, 1, n)
    make_second_group_to_sink(dinic.g, n+m+1, n+1, n+m)

    print(solution(dinic))


if __name__ == '__main__':
    main()
