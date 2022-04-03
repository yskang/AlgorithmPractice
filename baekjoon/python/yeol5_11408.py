# Title: 열혈강호5
# Link: https://www.acmicpc.net/problem/11408

import sys
from typing import List, Tuple
from collections import deque, defaultdict


def read_list_int() -> List[int]:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


INF = 10**10


def solution(n: int, m: int, tasks: List[Tuple[int, int]]) -> str:
    graph = [[] for _ in range(n+m+3)]
    flows = [[0 for _ in range(n+m+3)] for _ in range(n+m+3)]
    capacities = [[0 for _ in range(n+m+3)] for _ in range(n+m+3)]
    costs = [[0 for _ in range(n+m+3)] for _ in range(n+m+3)]

    source = 0
    sink = n + m + 1

    # make graph source to employees
    for i in range(1, n+1):
        graph[source].append(i)
        graph[i].append(source)
        capacities[source][i] = 1

    # make graph employees to sink
    for i in range(n+1, n+m+1):
        graph[i].append(sink)
        graph[sink].append(i)
        capacities[i][sink] = 1


    # make graph employees to tasks
    for e in range(1, n+1):
        for task, cost in tasks[e]:
            task = task + n
            graph[e].append(task)
            graph[task].append(e)
            capacities[e][task] = 1
            costs[e][task] = cost
            costs[task][e] = -cost

    result = 0
    cnt = 0

    while True:
        prev = [-1 for _ in range(m+n+3)]
        dist = [INF for _ in range(m+n+3)]
        visited = defaultdict(lambda: False)

        q = deque()
        dist[source] = 0
        visited[source] = True

        q.append(source)

        while q:
            current = q.popleft()
            visited[current] = False

            for child in graph[current]:
                flow, capacity, cost = flows[current][child], capacities[current][child], costs[current][child]
                if capacity - flow > 0 and dist[child] > dist[current] + cost:
                    dist[child] = dist[current] + cost
                    prev[child] = current
                    if not visited[child]:
                        q.append(child)
                        visited[child] = True

        if prev[sink] == -1:
            break

        currentflow = INF

        here = sink
        while here != source:
            before = prev[here]
            flow, capacity, cost = flows[before][here], capacities[before][here], costs[before][here]
            currentflow = min(currentflow, capacity - flow)
            here = before

        here = sink
        while here != source:
            before = prev[here]
            result += (currentflow * costs[before][here])
            flows[before][here] += currentflow
            flows[here][before] -= currentflow
            here = before

        cnt += 1

    return f'{cnt}\n{result}'


def main():
    n, m = read_list_int()
    tasks = [None]
    for _ in range(n):
        line = deque(read_list_int())
        size = line.popleft()
        temp = []
        for _ in range(size):
            temp.append((line.popleft(), line.popleft()))
        tasks.append(temp)
    print(solution(n, m, tasks))


if __name__ == '__main__':
    main()
