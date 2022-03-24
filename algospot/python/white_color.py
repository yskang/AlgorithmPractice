# Title: 화이트 칼라
# Link: https://www.acmicpc.net/problem/color

import sys
from collections import defaultdict
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


INF = 10**10


def dijkstra(start: int, child_of: defaultdict):
    pq = []
    distances = defaultdict(lambda: INF)
    path = defaultdict(lambda: [])

    distances[start] = 0
    heappush(pq, (0, start))

    while pq:
        distance, node = heappop(pq)

        if distances[node] < distance:
            continue

        for child, child_distance in child_of[node]:
            if distance + child_distance < distances[child]:
                distances[child] = distance + child_distance
                heappush(pq, (distance + child_distance, child))
                path[child].append(node)
            elif distance + child_distance == distances[child]:
                path[child].append(node)

    return path


def dfs(node: int, paths: defaultdict, visited: defaultdict):
    if visited[node]:
        return
    visited[node] = True
    for child in paths[node]:
        dfs(child, paths, visited)


def solution(n: int, m: int, child_of: defaultdict):
    paths = dijkstra(1, child_of)
    visited = defaultdict(lambda: False)
    dfs(n, paths, visited)
    ans = []
    for i in range(1, n+1):
        if visited[i]:
            ans.append(i)
    print(*ans)


def main():
    t = read_single_int()
    for _ in range(t):
        n, m = read_list_int()
        child_of = defaultdict(lambda: [])
        for _ in range(m):
            a, b = read_list_int()
            child_of[a].append((b, 1))
        solution(n, m, child_of)


if __name__ == '__main__':
    main()