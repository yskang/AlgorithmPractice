# Title: 열혈강호3
# Link: https://www.acmicpc.net/problem/11377

import sys
from collections import defaultdict, deque


sys.setrecursionlimit(10 ** 6)


def read_list_int(): return list(map(int, sys.stdin.readline().strip().split(' ')))


def bfs(g: defaultdict, level_of: list):
    # start node is 0
    queue = deque()
    queue.append(0)

    while queue:
        node = queue.popleft()
        level = level_of[node]

        for child in g[node].keys():
            if level_of[child] == -1 and g[node][child] > 0:
                level_of[child] = level+1
                queue.append(child)


def dfs(g: defaultdict, level_of: list, node: int, visited: defaultdict, paths: list, last_node: int, tot: list):
    if visited[node]:
        return
    visited[node] = True
    paths.append(node)

    for child in g[node].keys():
        if level_of[child] - level_of[node] == 1 and g[node][child] > 0:
            dfs(g, level_of, child, visited, paths, last_node, tot)

    if node == last_node:
        visited[node] = False
        min_capa = pow(10, 10)
        s = 0
        for node in paths[1:]:
            if g[s][node] < min_capa:
                min_capa = g[s][node]
            s = node
        tot[0] += min_capa
        # print('cal for {}, min is: {}'.format(paths, min_capa))
        s = 0
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
        level_of = [-1 for _ in range(sink+1)]
        level_of[source] = 0
        bfs(g, level_of)
        if level_of[sink] == -1:
            break

        visited = defaultdict(lambda: False)
        paths = []
        dfs(g, level_of, source, visited, paths, sink, s)
    return s[0]


def print_graph(g: defaultdict):
    for k in g:
        print('{} - [{}]'.format(k, g[k]))


def solution(g: defaultdict, source: int, sink: int):
    return dinic(g, source, sink)


def main():
    n, m, k = read_list_int()
    g = defaultdict(lambda: defaultdict(lambda: 0))
    
    source = 0
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

    print(solution(g, source, sink))


if __name__ == '__main__':
    main()