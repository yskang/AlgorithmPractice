# Title: 최소비용 구하기 2
# Link: https://www.acmicpc.net/problem/11779

import sys
from collections import defaultdict
from heapq import heappop, heappush


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
INF = 10**10


def dijkstra(start: int, child_of: defaultdict, end: int):
    costs = defaultdict(lambda: INF)
    paths = defaultdict(lambda: None)
    hq = []

    costs[start] = 0
    heappush(hq, (0, start))

    while hq:
        cost, node = heappop(hq)
        if costs[node] < cost:
            continue
        for child, child_cost in child_of[node]:
            if cost + child_cost < costs[child]:
                costs[child] = cost + child_cost
                heappush(hq, (cost + child_cost, child))
                paths[child] = node
    return paths, costs


def solution(n: int, m: int, child_of: defaultdict, start: int, end: int):
    path, costs = dijkstra(start, child_of, end)
    print(costs[end])
    ans = [end]
    while True:
        ans.append(path[ans[-1]])
        if ans[-1] == start:
            break
    print(len(ans))
    print(*reversed(ans))


def main():
    n = read_single_int()
    m = read_single_int()
    child_of = defaultdict(lambda: [])
    for _ in range(m):
        a, b, c = read_list_int()
        child_of[a].append((b, c))
    start, end = read_list_int()
    solution(n, m, child_of, start, end)


if __name__ == '__main__':
    main()