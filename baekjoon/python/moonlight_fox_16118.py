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
    path = collections.defaultdict(lambda: None)
    distance = collections.defaultdict(lambda: INF)
    pq = []

    distance[s] = 0
    heapq.heappush(pq, (s, 0))

    while pq:
        node, dist = heapq.heappop(pq)
        if distance[node] != dist:
            continue
        for (child, d) in graph.childs[node]:
            d *= 2
            if dist+d < distance[child]:
                distance[child] = dist+d
                path[child] = node
                heapq.heappush(pq, (child, dist+d))

    print(distance)
    print(path)


def dijkstra_wolf(graph: Graph, s: int):
    distance = collections.defaultdict(lambda: (INF, INF))
    pq = []
    distance[s] = (0, 0)
    heapq.heappush(pq, (s, 0))

    while pq:
        node, (d1, d2) = heapq.heappop(pq)
        # if distance[node] != dist:
        #     continue
        for (child, d) in graph.childs[node]:
            odd = d2 + d
            even = d1 + 4*d
            new_odd, new_even = d1, d2
            if odd < distance[child][0]:
                new_odd = odd                
            if even < distance[child][1]:
                new_even = even
            distance[child] = (new_odd, new_even)
            


    print(distance)



def solution(n: int, m: int, graph: Graph):
    dijkstra_fox(graph, 1)
    dijkstra_wolf(graph, 1)


def main():
    n, m = read_list_int()
    graph = Graph(n)
    for _ in range(m):
        graph.add_edge(*read_list_int())
    print(solution(n, m, graph))


if __name__ == '__main__':
    main()