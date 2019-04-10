# Title: 도시 왕복하기
# Link: https://www.acmicpc.net/problem/2316

import sys
from collections import defaultdict, deque


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def bfs(g: defaultdict, level_of: list, source: int):
    # start node is 0
    queue = deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        level = level_of[node]

        for child in g[node].keys():
            if level_of[child] == -1 and g[node][child] > 0:
                level_of[child] = level+1
                queue.append(child)


def dfs(g: defaultdict, level_of: list, node: int, visited: defaultdict, paths: list, source: int, sink: int, tot: list):
    if visited[node]:
        return
    visited[node] = True
    paths.append(node)

    for child in g[node].keys():
        if level_of[child] - level_of[node] == 1 and g[node][child] > 0:
            dfs(g, level_of, child, visited, paths, source, sink, tot)

    if node == sink:
        visited[node] = False
        min_capa = pow(10, 10)
        s = source
        for node in paths[1:]:
            if g[s][node] < min_capa:
                min_capa = g[s][node]
            s = node
        tot[0] += min_capa
        # print('cal for {}, min is: {}'.format(paths, min_capa))
        s = source
        for node in paths[1:]:
            g[s][node] -= min_capa
            g[node][s] += min_capa
            s = node

    paths.pop()


'''
start node      nodes group A           nodes group B             end node
--------------------------------------------------------------------------
      0 -----------> 0 ---------------------> 0 -------------------> 0
            -------> 0 ---------------------> 0 ------------------->
'''


def make_graph(source: int, sink: int, first_start: int, first_end: int, second_start: int, second_end: int):
    g = defaultdict(lambda: defaultdict(lambda: 0))
    make_source_to_first_group_one(g, source, first_start, first_end)
    make_second_group_to_sink(g, sink, second_start, second_end)
    return g


def make_source_to_first_group_one(g: defaultdict, source: int, group_start: int, group_end: int):
    for n in range(group_start, group_end+1):
        g[source][n] = 1
        g[n][source] = 0


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


def dinic(g: defaultdict, source: int, sink: int):
    s = [0]
    while True:
        level_of = [-1 for _ in range(len(g)+5)]
        level_of[source] = 0
        bfs(g, level_of, source)
        if level_of[sink] == -1:
            break

        visited = defaultdict(lambda: False)
        paths = []
        dfs(g, level_of, source, visited, paths, source, sink, s)
    return s[0]


def print_graph(g: defaultdict):
    for k in g:
        print('{} - [{}]'.format(k, g[k]))


def solution(g: defaultdict, source: int, sink: int):
    return dinic(g, source, sink)


def main():
    n, p = read_list_int()
    g = defaultdict(lambda: defaultdict(lambda: 0))
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

    print(solution(g, 1, 2))


if __name__ == '__main__':
    main()