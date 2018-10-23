# Title: 연결 요소의 개수
# Link: https://www.acmicpc.net/problem/11724

import sys

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class Graph:
    def __init__(self, n):
        self.childs = [[] for _ in range(n+1)]
    def add_node(self, a, b):
        self.childs[a].append(b)
        self.childs[b].append(a)


def dfs(g: Graph, n: int, visited: list):
    if visited[n]:
        return
    visited[n] = True
    visited[0] += 1
    for child in g.childs[n]:
        dfs(g, child, visited)


def solution(g: Graph, size: int):
    s = 0
    node = 1
    ans = 0
    visited = [0] + [False for _ in range(size)]
    for node in range(1, size+1):
        if visited[node]:
            continue
        dfs(g, node, visited)
        s += visited[0]
        ans += 1
    return ans


def main():
    N, M = read_list_int()
    g = Graph(N)
    for _ in range(M):
        u, v = read_list_int()
        g.add_node(u, v)
    if M == 0:
        print(N)
        return
    print(solution(g, N))


if __name__ == '__main__':
    main()