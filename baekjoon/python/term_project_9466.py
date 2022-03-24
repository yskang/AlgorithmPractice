# Title: 텀 프로젝트
# Link: https://www.acmicpc.net/problem/9466

import sys
import collections


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class Graph:
    def __init__(self, size: int):
        self.sel = [-1 for _ in range(size+1)]

    def add_node(self, student: int, select: int):
        self.sel[student] = select


def dfs(g: Graph, n: int, visited: list, path: list, idxs: collections.defaultdict):
    if visited[n]:
        path.append(n)
        return
    visited[n] = True
    path.append(n)
    idxs[n] = len(path)-1
    if g.sel[n] != -1:
        dfs(g, g.sel[n], visited, path, idxs)


def solution(n: int, g: Graph, iso: int):
    ans = n
    visited = [False for _ in range(n+1)]
    for node in range(1, n+1):
        if visited[node]:
            continue
        path = []
        idxs = collections.defaultdict(lambda:-1)
        dfs(g, node, visited, path, idxs)

        k = path.pop()
        if path != [] and idxs[k] != -1:
            ans -= len(path)-idxs[k]

    return ans - iso


def main():
    T = read_single_int()
    for _ in range(T):
        iso = 0
        n = read_single_int()
        students = read_list_int()
        g = Graph(n+1)
        for student, select in enumerate(students, 1):
            if student == select:
                iso += 1
            else:
                g.add_node(student, select)
        print(solution(n, g , iso))


if __name__ == '__main__':
    main()