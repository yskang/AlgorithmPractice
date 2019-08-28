# Title: 타임머신
# Link: https://www.acmicpc.net/problem/11657
import sys
from types import SimpleNamespace
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)

INF = 999999999999999

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, m: int, nodes: list):
    times = [INF for _ in range(n+1)]
    times[1] = 0
    starts = [1]
    for k in range(n+1):
        updated = []
        for start in starts:
            for child, time in nodes[start]:
                if times[child] > time+times[start]:
                    times[child] = time+times[start]
                    updated.append(child)
        if k == n and updated != []:
            print(-1)
            return
        starts, updated = updated, start
    for t in times[2:]:
        print(-1) if t == INF else print(t)


def shortest_path_faster_algorithm(s: int, nodes: list, n: int):
    dists = [INF for _ in range(n+1)]
    dists[s] = 0
    
    visites = defaultdict(lambda: False)
    cycles = defaultdict(lambda: 0)
    
    queue = deque()
    queue.append(s)
    visites[s] = True

    while queue:
        node = queue.popleft()
        visites[node] = False
        for child, w in nodes[node]:
            if dists[node] + w < dists[child]:
                dists[child] = dists[node] + w
                if not visites[child]:
                    cycles[child] += 1
                    if cycles[child] == n:
                        return -1
                    visites[child] = True
                    queue.append(child)
    return dists


def solution_spfa(n: int, m: int, nodes: list):
    dists = shortest_path_faster_algorithm(1, nodes, n)

    if dists == -1:
        print(-1)
    else:
        dists = list(map(lambda x: -1 if x == INF else x, dists))
        print(*dists[2:])


def main():
    n, m = read_list_int()
    nodes = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = read_list_int()
        nodes[a].append((b, c))
    solution_spfa(
        n, m, nodes)


if __name__ == '__main__':
    main()