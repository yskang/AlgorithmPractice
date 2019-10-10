# Title: LCA 2
# Link: https://www.acmicpc.net/problem/114438

import sys
from collections import defaultdict, deque


sys.setrecursionlimit(10 ** 6)
read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def dfs_init(node: int, child_of: list, parents: list, depth: int, visited: defaultdict, depths: list):
    visited[node] = True
    depths[node] = depth

    for child in child_of[node]:
        if visited[child]:
            continue
        parents[child][0] = node
        dfs_init(child, child_of, parents, depth+1, visited, depths)


def bfs_init(root: int, child_of: list, parents: list, depths: list):
    queue = deque()
    queue.append((root, 0))
    depths[root] = 0
    parents[root][0] = root
    while queue:
        parent, d = queue.popleft()
        for child in child_of[parent]:
            if depths[child] != -1:
                continue
            parents[child][0] = parent
            depths[child] = d+1
            queue.append((child, d+1))


def get_lca(a: int, b: int, depths: list, parents: list):
    if depths[a] > depths[b]:
        a, b = b, a
    for i in range(20, -1, -1):
        if depths[b] - depths[a] >= (1 << i):
            b = parents[b][i]
    if a == b:
        return a
    for i in range(20, -1, -1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]
    return parents[a][0]


def solution(n: int, child_of: list, m: int, ms: list):
    # visited = defaultdict(lambda: False)
    parents = [[-1 for _ in range(21)] for _ in range(n+1)]
    depths = [-1 for _ in range(n+1)]
    # dfs_init(1, child_of, parents, 0, visited, depths)
    bfs_init(1, child_of, parents, depths)

    for j in range(1, 21):
        for i in range(1, n+1):
            parents[i][j] = parents[parents[i][j-1]][j-1]

    for m1, m2 in ms:
        print(get_lca(m1, m2, depths, parents))


def main():
    n = read_single_int()
    child_of = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = read_list_int()
        child_of[a].append(b)
        child_of[b].append(a)
    m = read_single_int()
    ms = []
    for _ in range(m):
        ms.append(read_list_int())
    solution(n, child_of, m, ms)


if __name__ == '__main__':
    main()