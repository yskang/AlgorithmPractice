# Title: Network Delay Time
# Link: https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
from heapq import heappop, heappush
from typing import List

INF = 10**10

class Problem:
    def network_delay_time(self, times: List[List[int]], n: int, k: int) -> int:
        network = defaultdict(lambda: [])
        for start, end, time in times:
            network[start].append((end, time))

        min_times = self.dijkstra(network, k)
        ans = max(min_times.values())
        return -1 if len(min_times) != n else ans


    def dijkstra(self, graph: defaultdict, start: int):
        pq = []
        times = defaultdict(lambda: INF)

        times[start] = 0
        heappush(pq, (0, start))

        while pq:
            time, node = heappop(pq)
            if time != times[node]:
                continue
            for next_node, add_time in graph[node]:
                new_time = add_time + time
                if new_time < times[next_node]:
                    times[next_node] = new_time
                    heappush(pq, (new_time, next_node))

        return times


def solution():
    times = [[1,2,1],[2,3,2],[1,3,1]]
    n = 3
    k = 2
    problem = Problem()
    return problem.network_delay_time(times, n, k)


def main():
    print(solution())


if __name__ == '__main__':
    main()