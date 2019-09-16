# Title: 사회망 서비스(SNS)
# Link: https://www.acmicpc.net/problem/2533

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_min(node: int, is_early: int, dp: list, edges: defaultdict, p_node: int):
    if dp[node][is_early] != -1:
        return dp[node][is_early]
    
    res = is_early
    
    for child in edges[node]:
        if child == p_node:
            continue
        if is_early:
            res += min(get_min(child, 0, dp, edges, node), get_min(child, 1, dp, edges, node))
        else:
            res += get_min(child, 1, dp, edges, node)
    
    dp[node][is_early] = res
    return res


def solution(n: int, edges: defaultdict):
    dp = [[-1 for _ in range(2)] for _ in range(n+1)]
    max_value = min(get_min(1, 0, dp, edges, 0), get_min(1, 1, dp, edges, 0))

    return max_value


def main():
    n = read_single_int()
    edges = defaultdict(lambda: [])
    for _ in range(n-1):
        u, v = read_list_int()
        edges[u].append(v)
        edges[v].append(u)
    print(solution(n, edges))


if __name__ == '__main__':
    main()