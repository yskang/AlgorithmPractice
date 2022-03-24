# Title: 트리의 독립집합
# Link: https://www.acmicpc.net/problem/2213

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_max(node: int, select: int, n: int, ws: list, edges: defaultdict, dp: list, parent: int):
    if dp[node][select] != -1:
        return dp[node][select]
    
    ans = 0
    for child in edges[node]:
        if child != parent:
            if select == 1:
                ans += get_max(child, 0, n, ws, edges, dp, node)
            else:
                ans += max(get_max(child, 1, n, ws, edges, dp, node), get_max(child, 0, n, ws, edges, dp, node))
    dp[node][select] = ans + (ws[node] if select == 1 else 0)
    return dp[node][select]


def get_path(node: int, dp: list, paths: list, edges: defaultdict, select: list, f_node: int):
    if select == 1:
        paths.append(node)
        for child in edges[node]:
            if child != f_node:
                get_path(child, dp, paths, edges, 0, node)
    else:
        for child in edges[node]:
            if dp[child][0] <= dp[child][1]:
                if child != f_node:
                    get_path(child, dp, paths, edges, 1, node)
            else:
                if child != f_node:
                    get_path(child, dp, paths, edges, 0, node)


def solution(n: int, ws: list, edges: defaultdict):
    dp = [[-1 for _ in range(2)] for _ in range(n+1)]
    a, b = get_max(1, 0, n, ws, edges, dp, 0), get_max(1, 1, n, ws, edges, dp, 0)
    max_val = max(a, b)

    paths = []
    if a < b:
        get_path(1, dp, paths, edges, 1, 1)
    else:
        get_path(1, dp, paths, edges, 0, 1)

    return '{}\n{}'.format(max_val, ' '.join(map(str, sorted(paths))))


def main():
    n = read_single_int()
    ws = [0] + read_list_int()
    edges = defaultdict(lambda: [])
    for _ in range(n-1):
        a, b = read_list_int()
        edges[a].append(b)
        edges[b].append(a)
    print(solution(n, ws, edges))


if __name__ == '__main__':
    main()