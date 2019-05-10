from collections import defaultdict
import heapq


INF = pow(10, 10)-1


def dijkstra(graph: defaultdict, start: int):
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


if __name__ == '__main__':
    nodes = [[1, 2, 1],
            [1, 3, 2],
            [2, 3, 1]]
    graph = defaultdict(lambda: [])
    for a, b, weight in nodes:
        graph[a].append((b, weight))
        graph[b].append((a, weight))
    times = dijkstra(graph, 1)
    print(times)