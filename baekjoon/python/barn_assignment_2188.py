# Title: 축사 배정
# Link: https://www.acmicpc.net/problem/2188

import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


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
            g[node][s] = min_capa
            s = node

    paths.pop()


def log_info(g: defaultdict, N: int, M: int, level: list):
    print('graphs')
    for cow in range(M+1, M+N+1):
        print('{}: {}'.format(cow, list(g[cow].keys())))
    print('levels:')
    print(list(map(lambda i: '{}: {}'.format(i[0], i[1]) ,enumerate(level))))


def solution(N: int, M: int, g: defaultdict):
    # print(N, M)
    s = [0]
    while True:
        # 1. make level graph
        level_of = [-1 for _ in range(M+N+2)]
        level_of[0] = 0
        bfs(g, level_of)
        # log_info(g, N, M, level_of)
        if level_of[M+N+1] == -1:
            break
        
        # 2. do flow the current
        visited = defaultdict(lambda: False)
        paths = []
        dfs(g, level_of, 0, visited, paths, N+M+1, s)
        # log_info(g, N, M, level_of)
    return s[0]

def main():
    # g[a][b] = capacitance : capacitance of edge from a to b
    # g[a] = dictionary of childs
    # level_of = [leve]

    N, M = read_list_int()
    g = defaultdict(lambda: defaultdict(lambda: 0))
    for i in range(M+1, N+M+1):
        g[0][i] = 1
        g[i][0] = 0

    for i in range(M):
        g[i+1][N+M+1] = 1
        g[N+M+1][i+1] = 0

    for i in range(N):
        for b in read_list_int()[1:]:
            g[i+M+1][b] = 1
            g[b][i+M+1] = 0

    print(solution(N, M, g))


if __name__ == '__main__':
    main()