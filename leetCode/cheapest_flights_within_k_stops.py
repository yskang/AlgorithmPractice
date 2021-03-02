# Title: Cheapest Flights Withn K Stops
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List

INF = 10**10

class Problem:
    def find_cheapest_price(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(lambda: [])
        for start, end, time in flights:
            graph[start].append((end, time))
        return self.dijkstra(graph, src, dst, k)


    def dijkstra(self, graph: defaultdict, start: int, dst: int, k: int):
        pq = []
        heappush(pq, (0, start, k+1))

        while pq:
            cost, node, count = heappop(pq)
            if node == dst:
                return cost
            if count > 0:
                for child, time in graph[node]:
                    heappush(pq, (cost + time, child, count-1))

        return -1

def solution():
    n = 4
    edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    problem = Problem()
    return problem.find_cheapest_price(n, edges, src, dst, k)


def main():
    print(solution())


if __name__ == '__main__':
    main()