# Title: 효율적인 해킹
# Link: https://www.acmicpc.net/problem/1325

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def dfs(nodes, node, visited, count):
    if visited[node]:
        return
    visited[node] = True
    count[0] += 1
    for child in nodes[node]:
        dfs(nodes, child, visited, count)


def maximum_node(nodes, candidates, N):
    max_computer = 0
    max_nodes = []
    max_visits = []

    for node, valid in enumerate(candidates[1:], 1):
        if valid:
            count = [0]
            visited = [False] * (N + 1)

            dfs(nodes, node, visited, count)

            if count[0] > max_computer:
                max_computer = count[0]
                max_nodes = [node]
                max_visits = [visited]
            elif count[0] == max_computer:
                max_nodes.append(node)
                max_visits.append(visited)

    anothers = [False for _ in range(N+1)]
    for visited_log in max_visits:
        for node, visit in enumerate(visited_log[1:], 1):
            anothers[node] |= visit

    for node, visit in enumerate(anothers[1:], 1):
        if not visit:
            count = [0]
            visited = [False] * (N + 1)

            dfs(nodes, node, visited, count)

            if count[0] > max_computer:
                max_computer = count[0]
                max_nodes = [node]
                max_visits = [visited]
            elif count[0] == max_computer:
                max_nodes.append(node)
                max_visits.append(visited)

    return ' '.join(list(map(str, max_nodes)))


if __name__ == '__main__':
    N, M = read_list_int()
    nodes = [[] for _ in range(N + 1)]
    candidates = [True for _ in range(N + 1)]

    for _ in range(M):
        a, b = read_list_int()
        nodes[b].append(a)
        candidates[a] = False

    print(maximum_node(nodes, candidates, N))
