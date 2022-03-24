# Title: 책 나눠주기
# Link: https://www.acmicpc.net/problem/9576

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


def solution(n: int, m: int, adj: list):
    # us: students
    # vs: books
    us = [i for i in range(n+1, n+1+m+1)]
    hopcroft_karp = HopcroftKarp(us, adj)
    return hopcroft_karp.match()


def main():
    t = read_single_int()
    for _ in range(t):
        # n: books, m: students
        n, m = read_list_int()
        adj = [[] for _ in range(n+m+2)]
        for student in range(n+1, n+1+m):
            start, end = read_list_int()
            for book in range(start, end+1):
                adj[student].append(book)
                adj[book].append(student)
        print(solution(n, m, adj))


if __name__ == '__main__':  
    main()