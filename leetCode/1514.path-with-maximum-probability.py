#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

from typing import List
from collections import defaultdict
from heapq import heappush, heappop

INF = float('inf')

# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(lambda: [])
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        probs = self.dijkstra(graph, start_node)
        return probs[end_node]

    def dijkstra(self, graph: defaultdict, start: int):
        pq = []
        times = defaultdict(lambda: 0)
        times[start] = 1
        heappush(pq, (-1, start))
        while pq:
            prob, node = heappop(pq)
            prob = -prob
            if prob != times[node]:
                continue
            for next_node, add_prob in graph[node]:
                new_prob = add_prob * prob
                if new_prob > times[next_node]:
                    times[next_node] = new_prob
                    heappush(pq, (-new_prob, next_node))
        return times

# @lc code=end



def main():
    sol = Solution()
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    suceProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    print(sol.maxProbability(n, edges, suceProb, start, end))

    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    suceProb = [0.5, 0.5, 0.3]
    start = 0
    end = 2
    print(sol.maxProbability(n, edges, suceProb, start, end))

    n = 3
    edges = [[0, 1]]
    suceProb = [0.5]
    start = 0
    end = 2
    print(sol.maxProbability(n, edges, suceProb, start, end))


if __name__ == "__main__":
    main()
