# Title: 미확인 도착지
# Link: https://www.acmicpc.net/problem/9370

import sys
from collections import defaultdict, deque
from heapq import heappop, heappush


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
INF = 10**10


def dijkstra(start: int, child_of: defaultdict):
    hq = []
    distances = defaultdict(lambda: INF)
    paths = defaultdict(lambda: [])
    distances[start] = 0
    heappush(hq, (0, start))
    while hq:
        dist, node = heappop(hq)
        if distances[node] < dist:
            continue
        for child, child_dist in child_of[node]:
            if child_dist+dist < distances[child]:
                distances[child] = child_dist+dist
                heappush(hq, (child_dist+dist, child))
                paths[child] = [node]
            elif child_dist+dist == distances[child]:
                paths[child].append(node)
    return paths


def solution(n: int, m: int, t: int, s: int, g: int, h: int, child_of: defaultdict, targets: list):
    res = []
    paths = dijkstra(s, child_of)

    for target in targets:
        queue = deque()
        queue.append(target)
        is_find = False
        while queue and not is_find:
            node = queue.popleft()
            for child in paths[node]:
                if (node == g and child == h) or (node == h and child == g):
                    res.append(target)
                    is_find = True
                    break
                queue.append(child)            
    print(*sorted(res))


def main():
    T = read_single_int()
    for _ in range(T):
        n, m, t = read_list_int()
        s, g, h = read_list_int()
        child_of = defaultdict(lambda: [])
        for _ in range(m):
            a, b, d = read_list_int()
            child_of[a].append((b, d))
            child_of[b].append((a, d))
        targets = []
        for _ in range(t):
            x = read_single_int()
            targets.append(x)
        solution(n, m, t, s, g, h, child_of, targets)


if __name__ == '__main__':
    main()