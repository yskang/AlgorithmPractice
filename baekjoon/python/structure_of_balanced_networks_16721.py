# Title: Structure Of Balanced Networks
# Link: https://www.acmicpc.net/problem/16721

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


def read_single_int(): return int(sys.stdin.readline().strip())


def read_list_words(): return sys.stdin.readline().strip().split(' ')


def read_list_int(): return list(map(int, sys.stdin.readline().strip().split(' ')))


def find(x: int, parent: list):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x], parent)
        parent[x] = p
        return p


def union(x: int, y: int, parent: list):
    x = find(x, parent)
    y = find(y, parent)
    if x != y:
        parent[y] = x


def solution_union_find(n: int, parents: list, m: int, query: list):
    ans = []
    for a, b in query:
        if find(a, parents) == find(b, parents):
            ans.append('+')
        else:
            ans.append('-')
    return '\n'.join(ans)


def main_union_find():
    n = read_single_int()
    parents = [i for i in range(n)]
    for r in range(n):
        for c, v in enumerate(read_list_words()):
            if v == '+':
                union(r, c, parents)
    m = read_single_int()
    query = []
    for _ in range(m):
        query.append(read_list_int())
    print(solution_union_find(n, parents, m, query))


def solution(n: int, side: list, m: int, query: list):
    ans = []
    for a, b in query:
        ans.append('+') if side[a] == side[b] else ans.append('-')
    return '\n'.join(ans)


def main():
    n = read_single_int()
    side = []
    for v in read_list_words():
        side.append(False) if v == '-' else side.append(True)
    for _ in range(n-1):
        sys.stdin.readline()

    m = read_single_int()
    query = []
    for _ in range(m):
        query.append(read_list_int())
    print(solution(n, side, m, query))


if __name__ == '__main__':
    # main_union_find()
    main()
