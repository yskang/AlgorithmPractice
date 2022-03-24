import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 6)


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


def solution(ns: list, adj: defaultdict):
    hopcroft_karp = HopcroftKarp(ns, adj)
    return hopcroft_karp.match()


def main():
    n, m = read_list_int()
    ns = [i+m+1 for i in range(n)]
    adj = defaultdict(lambda: [])
    
    for i in range(n):
        adj[i+1+m] = read_list_int()[1:]

    print(solution(ns, adj))


if __name__ == '__main__':
    main()