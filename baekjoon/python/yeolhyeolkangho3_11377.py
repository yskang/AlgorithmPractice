# Title: 열혈강호3
# Link: https://www.acmicpc.net/problem/11377

import sys
from collections import defaultdict, deque


sys.setrecursionlimit(10 ** 6)


def read_list_int(): return list(map(int, sys.stdin.readline().strip().split(' ')))

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

    def get_graph(self):
        return self.g

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


def solution(dinic: Dinic):
    return dinic.get_maximum_flow()


def main():
    n, m, k = read_list_int()
    dinic = Dinic(0, n+m+2)
    g = dinic.get_graph()
    
    knode = n+m+1
    sink = n+m+2

    g[0][knode] = k
    g[knode][0] = 0

    for i in range(1, n+1):
        works = read_list_int()
        g[0][i] = 1
        g[i][0] = 0

        g[knode][i] = 1
        g[i][knode] = 0

        for work in works[1:]:
            g[i][work+n] = 1
            g[work+n][i] = 0

    for i in range(n+1, n+m+1):
        g[i][sink] = 1
        g[sink][i] = 0

    print(solution(dinic))


if __name__ == '__main__':
    main()