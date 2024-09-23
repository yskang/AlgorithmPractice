#
# @lc app=leetcode id=2699 lang=python3
#
# [2699] Modify Graph Edge Weights
#
from typing import List
from collections import defaultdict
import heapq

INF = pow(10, 10)-1

# @lc code=start
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = defaultdict(lambda: [])
        for a, b, weight in edges:
            graph[a].append((b, weight))
            graph[b].append((a, weight))
        
        

    def dijkstra(self, graph: defaultdict, start: int):
        pq = []
        times = defaultdict(lambda: INF)

        times[start] = 0
        heapq.heappush(pq, (0, start))

        while pq:
            time, node = heapq.heappop(pq)
            if time != times[node]:
                continue
            for next_node, add_time in graph[node]:
                new_time = add_time + time
                if new_time < times[next_node]:
                    times[next_node] = new_time
                    heapq.heappush(pq, (new_time, next_node))

        return times

    
        
# @lc code=end


def main():
    sol = Solution()
    n = 5
    edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
    source = 0
    destination = 1
    target = 5
    print(sol.modifiedGraphEdges(n, edges, source, destination, target))
    

if __name__ == "__main__":
    main()    
