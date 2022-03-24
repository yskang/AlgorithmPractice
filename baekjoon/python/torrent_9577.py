# Title: 토렌트
# Link: https://www.acmicpc.net/problem/9577

import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


INF = pow(10, 10)
NIL = -1


class HopcroftKarp:
    def __init__(self, us: list, adj: list):
        self.us = us
        self.adj = adj

    def bfs(self, pair_u: defaultdict, pair_v: defaultdict, dist: defaultdict):
        queue = deque()
        for u in self.us:
            if pair_u[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[NIL] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v in self.adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[NIL] != INF

    def dfs(self, u: int, dist: defaultdict, pair_v: defaultdict, pair_u: defaultdict):
        if u != NIL:
            for v in self.adj[u]:
                if dist[pair_v[v]] == dist[u]+1:
                    if self.dfs(pair_v[v], dist, pair_v, pair_u):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    def match(self):
        dist = defaultdict(lambda: NIL)
        pair_u = defaultdict(lambda: NIL)
        pair_v = defaultdict(lambda: NIL)
        matching = 0
        while self.bfs(pair_u, pair_v, dist):
            for u in self.us:
                if pair_u[u] == NIL:
                    if self.dfs(u, dist, pair_v, pair_u):
                        matching += 1
        return matching


def solution(times: list, adj: list, num_parts: int):
    for i in range(101):
        temp_adj = defaultdict(lambda: [])
        for t in range(i+1):
            temp_adj[t] = adj[t]
        for p in range(201, 301):
            temp_adj[p] = list(filter(lambda t: t<=i, adj[p]))
        hopcroft_karp = HopcroftKarp(times[:i+1], temp_adj)
        count = hopcroft_karp.match()
        if count == num_parts:
            return i+1
    return -1


def main():
    t = read_single_int()
    for _ in range(t):
        n, m = read_list_int()
        times = [i for i in range(0, 101)]
        adj = [set() for _ in range(301)]
        for _ in range(m):
            seed = read_list_int()
            t1 = seed[0]
            t2 = seed[1] 
            qs = seed[3:]
            for time in range(t1, t2):
                for q in qs:
                    adj[time].add(q+200)
                    # adj[q+200].add(time)
        for i, child in enumerate(adj):
            adj[i] = sorted(list(child))
        
        print(solution(times, adj, n))

if __name__ == '__main__':
    main()