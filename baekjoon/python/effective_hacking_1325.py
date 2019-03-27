# Title: 효율적인 해킹
# Link: https://www.acmicpc.net/problem/1325

import sys
import copy
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def dfs(graph: list, n: int, visited: list, stack: list):
    if visited[n]:
        return
    visited[n] = True

    for ch in graph[n]:
        dfs(graph, ch, visited, stack)

    stack.append(n)


def maximum_node(N: int, graph: list, graph_reverse: list, start_nodes: list):
    stack = []
    visited = [False for _ in range(N+1)]

    for node in range(1, N+1):
        if start_nodes[node]:
            dfs(graph, node, visited, stack)
            if len(stack) == N:
                break

    if len(stack) != N:
        for node, is_visit in enumerate(visited[1:], 1):
            if not is_visit:
                dfs(graph, node, visited, stack)
            if len(stack) == N:
                break

    visited = [False for _ in range(N+1)]
    map_table = [i for i in range(N+1)]
    count_table = [[i] for i in range(N+1)]

    for node in reversed(stack):
        temp = []
        dfs(graph_reverse, node, visited, temp)
        sorted_temp = sorted(temp)
        if temp:
            count_table[sorted_temp[0]] = sorted_temp
            for node in temp:
                map_table[node] = sorted_temp[0]

    start_nodes = [True for _ in range(N+1)]
    for i, nodes in enumerate(graph[1:], 1):
        childs = set()
        for node in nodes:
            childs.add(map_table[node])
        if map_table[i] == i:
            graph[i] = list(childs)
        else:
            new_i = map_table[i]
            l = set(graph[new_i]).union(childs)
            l.discard(new_i)
            graph[new_i] = list(l)
            graph[i] = []

    for n, childs in enumerate(graph[1:], 1):
        for child in childs:
            start_nodes[child] = False

    max_nodes = []
    max_count = 0
    for n in range(1, N+1):
        if start_nodes[n] == True:
            visits = []
            has_visit = defaultdict(lambda: False)
            dfs(graph, n, has_visit, visits)
            count = 0
            for visit in visits:
                count += len(count_table[visit])

            if count > max_count:
                max_count = count
                max_nodes = [n]
            elif count == max_count:
                max_nodes.append(n)

    results = []
    for node in max_nodes:
        results += count_table[node]

    return ' '.join(map(str, sorted(results)))


def main():
    N, M = read_list_int()
    graph = [[] for _ in range(N+1)]
    graph_reverse = [[] for _ in range(N+1)]
    start_nodes = [True for i in range(N+1)]

    for _ in range(M):
        a, b = read_list_int()
        graph[b].append(a)
        graph_reverse[a].append(b)
        start_nodes[a] = False

    print(maximum_node(N, graph, graph_reverse, start_nodes))


if __name__ == '__main__':
    main()
