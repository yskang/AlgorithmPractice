# Title: 달빛 여우
# Link: https://www.acmicpc.net/problem/16118

import sys
import collections
import heapq


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

INF = 999999999999999

class Graph:
    def __init__(self, n: int):
        self.childs = [[] for _ in range(n+1)]

    def add_edge(self, a: int, b: int, d: int):
        self.childs[a].append((b, d))
        self.childs[b].append((a, d))

    def __str__(self):
        return str(self.childs)


def dijkstra_fox(graph: Graph, s: int):
    distance = collections.defaultdict(lambda: INF)
    pq = []

    distance[s] = 0
    heapq.heappush(pq, (0, s))

    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node] < dist:
            continue
        for (child, d) in graph.childs[node]:
            d *= 2
            if dist+d < distance[child]:
                distance[child] = dist+d
                heapq.heappush(pq, (dist+d, child))

    # print(distance)
    return distance

F_SLOW = True
F_QUICK = False

def dijkstra_wolf(graph: Graph, s: int, n: int):
    distance = [[INF, INF] for _ in range(n+1)]
    pq = []

    distance[s] = [0, INF] #slow, quick
    heapq.heappush(pq, [0, F_SLOW, s]) # distance, prev speed, node

    while pq:
        dist, prev, node = heapq.heappop(pq)

        if prev == F_QUICK and distance[node][1] < dist:
            continue
        if prev == F_SLOW and distance[node][0] < dist:
            continue

        for (child, d) in graph.childs[node]:
            if prev == F_QUICK:
                new_dist = dist + 4*d
            else:
                new_dist = dist + d

            if prev == F_QUICK and new_dist < distance[child][0]:
                distance[child][0] = new_dist
                heapq.heappush(pq, [new_dist, F_SLOW, child])
            elif prev == F_SLOW and new_dist < distance[child][1]:
                distance[child][1] = new_dist
                heapq.heappush(pq, [new_dist, F_QUICK, child])
    
    # print(distance)
    return distance


def solution(n: int, m: int, graph: Graph):
    fox = dijkstra_fox(graph, 1)
    wolf = dijkstra_wolf(graph, 1, n)
    count = 0
    for g in range(1, n+1):
        if fox[g] < min(wolf[g]):
            count += 1
    return count


def main():
    n, m = read_list_int()
    graph = Graph(n)
    for _ in range(m):
        graph.add_edge(*read_list_int())
    print(solution(n, m, graph))


if __name__ == '__main__':
    main()