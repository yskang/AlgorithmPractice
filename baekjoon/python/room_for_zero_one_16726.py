# Title: 영과 일의 학회방
# Link: https://www.acmicpc.net/problem/16726

import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_str = lambda: sys.stdin.readline().strip()

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


def solution(rows: int, columns: int, room: list):
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    evens = []
    odds = []
    adj = [[] for _ in range(rows*columns)]
    total = 0
    for r in range(rows):
        for c in range(columns):
            if room[r][c] != 'X':
                total += 1
                number = c + columns*r
                if (r+c) % 2 == 0:
                    evens.append(number)
                else:
                    odds.append(number)
                
                for off_x, off_y in offsets:
                    xx, yy = c + off_x, r + off_y
                    if 0 <= xx < columns and 0 <= yy < rows and room[yy][xx] != 'X':
                        adj[number].append(xx + columns*yy)

    hopcroft_karp = HopcroftKarp(evens, adj)
    max_match = hopcroft_karp.match()
    return total - max_match


def main():
    n, m = read_list_int()
    room = []
    for _ in range(n):
        room.append(list(read_single_str()))

    print(solution(n, m, room))


if __name__ == '__main__':
    main()