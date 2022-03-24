import sys
from collections import defaultdict, deque


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

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
    n, p = read_list_int()
    dinic = Dinic(1, 2)
    g = dinic.get_graph()
    for _ in range(p):
        a, b = read_list_int()
        if a != 1 and a != 2:
            g[a][a+n] = 1
            g[a+n][a] = 0
        if b != 1 and b != 2:
            g[b][b+n] = 1
            g[b+n][b] = 0
        if a == 1 or a == 2:
            g[a][b] = 1
            g[b][a] = 0
            g[b+n][a] = 1
            g[a][b+n] = 0
        elif b == 1 or b == 2:
            g[a+n][b] = 1
            g[b][a+n] = 0
            g[b][a] = 1
            g[a][b] = 0
        else:
            g[a+n][b] = 1
            g[b][a+n] = 0
            g[b+n][a] = 1
            g[a][b+n] = 0

    print(solution(dinic))


if __name__ == '__main__':
    main()