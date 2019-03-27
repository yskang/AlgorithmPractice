# Title: 핼렬 곱셈
# Link: https://www.acmicpc.net/problem/15933

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def find(x: int, parent: defaultdict):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x], parent)
        parent[x] = p
        return p

def union(x: int, y: int, parent: defaultdict):
    x = find(x, parent)
    y = find(y, parent)
    if x != y:
        parent[y] = x


def solution(n: int, g: defaultdict, nodes: list, indegrees: defaultdict, outdegrees: defaultdict):
    zeros = []
    ones = []
    minus_ones = []
    for node in nodes:
        degree = indegrees[node] - outdegrees[node]
        if degree == 0:
            zeros.append(node)
        elif degree == 1:
            ones.append(node)
        elif degree == -1:
            minus_ones.append(node)
    
    if len(zeros) + len(ones) + len(minus_ones) != len(nodes):
        return 0

    if len(zeros) == len(nodes):
        return max(nodes)**2
    elif len(ones) == 1 and len(minus_ones) == 1:
        return ones[0] * minus_ones[0]
    else:
        return 0
    

def main():
    n = read_single_int()
    g = defaultdict(lambda: [])
    nodes = set()
    indegrees = defaultdict(lambda: 0)
    outdegrees = defaultdict(lambda: 0)
    parent = [i for i in range(1001)]

    for _ in range(n):
        a, b = read_list_int()
        nodes.add(a)
        nodes.add(b)
        g[a].append(b)
        outdegrees[a] += 1
        indegrees[b] += 1
        union(a, b, parent)
        all_parents = set()
        for node in nodes:
            all_parents.add(find(node, parent))

        if len(all_parents) != 1:
            print(0)
        else:
            print(solution(n, g, nodes, indegrees, outdegrees))


if __name__ == '__main__':
    main()    