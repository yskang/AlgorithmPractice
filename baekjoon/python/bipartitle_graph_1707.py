# Title: 이분 그래프
# Link: https://www.acmicpc.net/problem/1707

import sys
import collections

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class Graph:
    def __init__(self):
        self.childs = collections.defaultdict(lambda: [])

    def add_node(self, a: int, b: int):
        self.childs[a].append(b)
        self.childs[b].append(a)


def dfs(g: Graph, n: int, visited: list, colors: list, current_color: int, is_bg: []):
    if visited[n]:
        if colors[n] != current_color:
            is_bg[0] = False
        return
    visited[n] = True
    colors[n] = current_color
    next_color = 2 if current_color == 1 else 1
    for child in g.childs[n]:
        dfs(g, child, visited, colors, next_color, is_bg)


def solution(g: Graph, s: int):
    is_bg = [True]
    visited = [0] + [False for _ in range(s)]
    colors = [0 for _ in range(s+1)]
    for node in range(1, s+1):
        if visited[node]:
            continue
        dfs(g, node, visited, colors, 1, is_bg)
        if is_bg[0] == False:
            return 'NO'
    return 'YES'


def main():
    k = read_single_int()
    for _ in range(k):
        g = Graph()
        v, e = read_list_int()
        for _ in range(e):
            y, z = read_list_int()
            g.add_node(y, z)
        print(solution(g, v))


if __name__ == '__main__':
    main()