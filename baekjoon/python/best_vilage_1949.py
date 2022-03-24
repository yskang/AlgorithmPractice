# Title: 우수 마을
# Link: https://www.acmicpc.net/problem/1949

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_max(vil: int, select: int, dp: list, edges: defaultdict, popls: list, p_node: int):
    if dp[vil][select] != -1:
        return dp[vil][select]
    
    ans = popls[vil] if select else 0

    for child in edges[vil]:
        if child == p_node:
            continue
        if select:
            ans += get_max(child, 0, dp, edges, popls, vil)
        else:
            ans += max(get_max(child, 0, dp, edges, popls, vil), get_max(child, 1, dp, edges, popls, vil))

    dp[vil][select] = ans
    return ans


def solution(n: int, popls: list, edges: defaultdict):
    dp = [[-1 for _ in range(2)] for _ in range(n+1)]
    return max(get_max(1, 0, dp, edges, popls, 0), get_max(1, 1, dp, edges, popls, 0))
    

def main():
    n = read_single_int()
    popls = [0] + read_list_int()
    edges = defaultdict(lambda: [])
    for _ in range(n-1):
        a, b = read_list_int()
        edges[a].append(b)
        edges[b].append(a)
    print(solution(n, popls, edges))


if __name__ == '__main__':
    main()