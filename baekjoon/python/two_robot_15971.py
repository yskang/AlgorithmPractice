# Title: 두 로봇
# Link: https://www.acmicpc.net/problem/15971

import sys
from collections import defaultdict, deque
from types import SimpleNamespace
from copy import deepcopy


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


paths = []
ans = 0


def dfs(node: int, target: int, f_node: int, adjs: defaultdict):
    global paths
    global ans

    if node == target:
        if len(paths) > 1:
            ans = sum(paths)-max(paths)
        else:
            ans = 0
        return

    for adj, dist in adjs[node]:
        if adj != f_node:
            paths.append(dist)
            dfs(adj, target, node, adjs)
    
    if paths:
        paths.pop()


def solution(n: int, r1: int, r2: int, adjs: defaultdict):
    if n == 1 or r1 == r2:
        return 0
    dfs(r1, r2, None, adjs)
    return ans


def solution_bfs(n: int, r1: int, r2: int, adjs: defaultdict):
    max_distance = defaultdict(lambda: -1)
    distance = defaultdict(lambda: 0)

    if n == 1 or r1 == r2:
        return 0

    q = deque()
    q.append((None, r1))

    while q:
        f_node, node = q.popleft()
        if node == r2:
            return distance[node] - max_distance[node]

        for adj, dist in adjs[node]:
            if adj != f_node:
                max_distance[adj] = max(max_distance[node], dist)
                distance[adj] = distance[node] + dist
                q.append((node, adj))
    return


def main():
    n, r1, r2 = read_list_int()
    adjs = defaultdict(lambda: [])
    for _ in range(n-1):
        a, b, d = read_list_int()
        adjs[a].append((b, d))
        adjs[b].append((a, d))
    print(solution_bfs(n, r1, r2, adjs))


if __name__ == '__main__':
    main()