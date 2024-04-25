# Title: 정훈이는 민트초코맛 짜장라면이 먹고 싶다.
# Link: https://www.acmicpc.net/problem/23975

import sys
from heapq import heappop, heappush


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def djikstra(start: int, graph: list):
    dist = [float('inf') for _ in range(len(graph))]
    path = [float('inf') for _ in range(len(graph))]
    dist[start] = 0
    queue = []
    heappush(queue, (0, start))
    while queue:
        cost, node = heappop(queue)
        node = -node
        if dist[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heappush(queue, (new_cost, -next_node))
                path[next_node] = node
            # elif new_cost == dist[next_node]:
            #     path[next_node] = max(node, path[next_node])
    return dist, path


def solution(n: int, m: int, k: int, left_ramens: list, graph: list, junghoon_position: list):
    left_ramens = [0] + left_ramens
    _, path = djikstra(1, graph)
    for start in junghoon_position:
        temp_path = []
        if start == 1:
            if left_ramens[start] > 0:
                left_ramens[start] -= 1
                print(start)
                continue
            else:
                print(-1)
                continue
        if path[start] == float('inf'):
            print(-1)
            continue
        current = start
        while True:
            if current == float('inf'):
                print(-1)
                break
            if left_ramens[current] > 0:
                left_ramens[current] -= 1
                print(current)
                if current != start:
                    for p in temp_path:
                        path[p] = current
                break
            if current == 1:
                print(-1)
                if current != start:
                    for p in temp_path:
                        path[p] = current
                break
            temp_path.append(current)
            current = path[current]
    return


def main():
    n, m, k = read_list_int()
    left_ramens = read_list_int()
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = read_list_int()
        graph[a].append((b, c))
        graph[b].append((a, c))
    junghoon_position = []
    for _ in range(k):
        junghoon_position.append(read_single_int())
    solution(n, m, k, left_ramens, graph, junghoon_position)


if __name__ == '__main__':
    main()