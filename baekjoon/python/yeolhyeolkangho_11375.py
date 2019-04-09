# Title: 열혈강호
# Link: https://www.acmicpc.net/problem/11375

import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))



INF = pow(10, 10)
NIL = -1

def bfs(us: list, pair_u: defaultdict, pair_v: defaultdict, dist: defaultdict, adj: list):
    queue = deque()
    for u in us:
        if pair_u[u] == NIL:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = INF
    dist[NIL] = INF
    while queue:
        u = queue.popleft()
        if dist[u] < dist[NIL]:
            for v in adj[u]:
                if dist[pair_v[v]] == INF:
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
    return dist[NIL] != INF


def dfs(u: int, adj: list, dist: defaultdict, pair_v: defaultdict, pair_u: defaultdict):
    if u != NIL:
        for v in adj[u]:
            if dist[pair_v[v]] == dist[u]+1:
                if dfs(pair_v[v], adj, dist, pair_v, pair_u):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
        dist[u] = INF
        return False
    return True


def hopcroft_karp(us: list, adj: list):
    dist = defaultdict(lambda: NIL)
    pair_u = defaultdict(lambda: NIL)
    pair_v = defaultdict(lambda: NIL)
    matching = 0
    while bfs(us, pair_u, pair_v, dist, adj):
        for u in us:
            if pair_u[u] == NIL:
                if dfs(u, adj, dist, pair_v, pair_u):
                    matching += 1
    return matching


def solution(ns: list, adj: defaultdict):
    return hopcroft_karp(ns, adj)


def main():
    n, m = read_list_int()
    ns = [i+m+1 for i in range(n)]
    adj = defaultdict(lambda: [])
    
    for i in range(n):
        adj[i+1+m] = read_list_int()[1:]

    print(solution(ns, adj))


if __name__ == '__main__':
    main()