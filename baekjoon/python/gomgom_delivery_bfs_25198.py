# Title: 곰곰이의 심부름
# Link: https://www.acmicpc.net/problem/25198

import sys
from collections import defaultdict, deque
from math import comb


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, s: int, c: int, h: int, g: defaultdict):
    nodes = [0 for _ in range(n+1)]
    q = deque()
    q.append((s, 0))  # node, before
    while q:
        node, before = q.popleft()
        nodes[node] = before
        if node == c:
            break
        for child in g[node]:
            if child != before:
                q.append((child, node))

    sc_path = [c]
    while True:
        sc_path.append(nodes[sc_path[-1]])
        if sc_path[-1] == s:
            break
        elif sc_path[-1] == 0:
            return 0

    nodes = [0 for _ in range(n+1)]
    q = deque()
    q.append((c, 0))  # node, before

    while q:
        node, before = q.popleft()
        nodes[node] = before
        if node == h:
            break
        for child in g[node]:
            if child != before:
                q.append((child, node))

    ch_path = [h]
    while True:
        ch_path.append(nodes[ch_path[-1]])
        if ch_path[-1] == c:
            break
        elif ch_path[-1] == 0:
            return 0

    ch_path.reverse()
    duplications = 0
    for i in range(min(len(sc_path), len(ch_path))):
        if sc_path[i] == ch_path[i]:
            duplications += 1
        else:
            break

    return comb(len(sc_path) + len(ch_path) - duplications, 2) + comb(duplications, 2)


def main():
    n = read_single_int()
    s, c, h = read_list_int()
    g = defaultdict(lambda: [])
    for _ in range(n-1):
        u, v = read_list_int()
        g[u].append(v)
        g[v].append(u)
    print(solution(n, s, c, h, g))


if __name__ == '__main__':
    main()