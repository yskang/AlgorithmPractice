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


def dfs(n: int, visited: list):
    if visited[n]:
        return
    visited[n] = True

    for ch in graph[n]:
        dfs(ch, visited)
    
    stack.append(n)


def dfs_r(n: int, visited: list, scc: list):
    if visited[n]:
        return
    visited[n] = True

    for ch in r_graph[n]:
        dfs_r(ch, visited, scc)

    scc.append(n)


def maximum_node(N: int):
    map_table = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    candis = [True for _ in range(N+1)]
    t_visited = copy.deepcopy(visited)

    t_visited[0] = True
    for node in range(1, N+1):
        dfs(node, t_visited)
        if all(t_visited):
            break

    t_visited = copy.deepcopy(visited)
    for node in reversed(stack):
        temp = []
        dfs_r(node, t_visited, temp)
        sorted_temp = sorted(temp)

        if temp:
            for t in temp:
                map_table[t] = sorted_temp
            for t in sorted_temp[1:]:
                candis[t] = False

    for a, b in inputs:
        a = map_table[a][0]
        b = map_table[b][0]
        if a != b:
            mod_graph[b].add(a)
            candis[a] = False

    child_nums = defaultdict(lambda: [])
    for node, trusted in enumerate(candis[1:], 1):
        if trusted:
            t_visited = copy.deepcopy(visited)
            count = [0]
            get_num_child(node, map_table, t_visited, count)
            child_nums[count[0]].append(node)

    max_nodes = set(child_nums[sorted(child_nums.keys(), reverse=True)[0]])
    results = set()
    for node in max_nodes:
        results.update(map_table[node])
    
    return ' '.join(map(str, sorted(results)))


def get_num_child(node: int, map_table: list, visited: list, count: list):
    if visited[node]:
        return

    visited[node] = True

    for child in mod_graph[node]:
        get_num_child(map_table[child][0], map_table, visited, count)

    count[0] += len(map_table[node])
    return


if __name__ == '__main__':
    N, M = read_list_int()
    graph = [set() for _ in range(N+1)]
    r_graph = [set() for _ in range(N+1)]
    mod_graph = [set() for _ in range(N+1)]
    stack = []
    inputs = []

    for _ in range(M):
        a, b = read_list_int()
        graph[b].add(a)
        r_graph[a].add(b)
        inputs.append((a, b))

    print(maximum_node(N))
