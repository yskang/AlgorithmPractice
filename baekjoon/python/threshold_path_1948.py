# Title: 임계 경로
# Link: https://www.acmicpc.net/problem/1948

import sys
from heapq import heappop, heappush
from collections import deque


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def dijkstra(start: int, graph: list) -> tuple:
    dists = [0 for _ in range(len(graph))]
    paths = [[] for _ in range(len(graph))]
    queue = []
    heappush(queue, (0, start))  # (dist, node)

    while queue:
        dist, node = heappop(queue)
        if dist > dists[node]:
            continue
        dists[node] = dist
        for next_node, next_dist in graph[node]:
            new_dist = dist + next_dist
            if new_dist < dists[next_node]:
                dists[next_node] = new_dist
                paths[next_node] = [node]
                heappush(queue, (new_dist, next_node))
            elif new_dist == dists[next_node]:
                paths[next_node].append(node)

    return dists, paths


def solution(n: int, m: int, graph: list, start: int, destination: int) -> str:
    dist, path = dijkstra(start, graph)
    count_road = 0
    max_dist = -dist[destination]

    q = deque()
    q.append(destination)
    visited = [False for _ in range(n+1)]
    while q:
        node = q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        if node == start:
            break
        for prev_node in path[node]:
            count_road += 1
            q.append(prev_node)

    return (f'{max_dist}\n{count_road}')


def main():
    n = read_single_int()
    m = read_single_int()
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = read_list_int()
        graph[a].append((b, -c))
    start, destination = read_list_int()
    print(solution(n, m, graph, start, destination))


if __name__ == '__main__':
    main()