# Title: 트리와 쿼리
# Link: https://www.acmicpc.net/problem/15681

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def count_childs(node: int, edges: defaultdict, visited: defaultdict, subs: list):
    if visited[node]:
        return 0
    visited[node] = True
    count = 1
    for child in edges[node]:
        count += count_childs(child, edges, visited, subs)
    subs[node] = count
    return count


def solution(n: int, r: int, q: int, edges: defaultdict, queries: list):
    visited = defaultdict(lambda: False)
    subs = [0 for _ in range(n+1)]
    count_childs(r, edges, visited, subs)
    for query in queries:
        print(subs[query])


def main():
    n, r, q = read_list_int()
    edges = defaultdict(lambda: [])
    for _ in range(n-1):
        u, v = read_list_int()
        edges[u].append(v)
        edges[v].append(u)
    queries = []
    for _ in range(q):
        queries.append(read_single_int())
    solution(n, r, q, edges, queries)


if __name__ == '__main__':
    main()