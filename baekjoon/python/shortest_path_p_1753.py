# Title: 문제제목
# Link: https://www.acmicpc.net/problem/1753

import sys
from collections import defaultdict as ddict
import heapq

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


INF = 9999999999999


class Graph:
    def __init__(self, size: int):
        self.childs = [set() for _ in range(size+1)]
        self.edges = ddict(lambda: INF)

    def add_edge(self, start: int, end: int, weight: int):
        self.childs[start].add(end)
        self.edges[(start, end)] = min(self.edges[(start, end)], weight)


def dijkstra(g: Graph, s: int):
    distance = ddict(lambda: INF)
    pq = []
    
    distance[s] = 0
    heapq.heappush(pq, (0, s))

    while pq:
        dist, node = heapq.heappop(pq)

        if distance[node] != dist:
            continue

        for child in g.childs[node]:
            weight = g.edges[(node, child)]
            if distance[child] > dist + weight:
                distance[child] = dist + weight
                heapq.heappush(pq, (dist+weight, child))

    return distance


def solution(g: Graph, s: int, v: int, e: int):
    distance = dijkstra(g, s)
    ans = []
    for n in range(v):
        d = distance[n+1]
        if d != INF:
            ans.append(str(d))
        else:
            ans.append('INF')
    return '\n'.join(ans)


def main():
    v, e = read_list_int()
    s = read_single_int()
    g = Graph(v)
    for _ in range(e):
        a, b, w = read_list_int()
        g.add_edge(a, b, w)
    print(solution(g, s, v, e))


if __name__ == '__main__':
    main()