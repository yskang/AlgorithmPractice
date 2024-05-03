# Title: 트리
# Link: https://www.acmicpc.net/problem/10838

import sys


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def get_lca(parents: list, a: int, b: int) -> int:
    if a == b:
        return a
    if a == 0 or b == 0:
        return 0

    parents_a = set()
    parents_b = set()

    while True:
        parents_a.add(a)
        parents_b.add(b)

        if b in parents_a:
            return b
        if a in parents_b:
            return a
        a = parents[a][0]
        b = parents[b][0]


def solution(n: int, k: int, quries: list):
    parents = [[0, 0] for _ in range(n)]  # [parent, color]
    for query in quries:
        if query[0] == 1:
            a, b, c = query[1], query[2], query[3]
            # find lca node of a and b
            # and, paint all nodes from a to lca with c
            # and paint all nodes from b to lca with c
            lca = get_lca(parents, a, b)
            while a != lca:
                parents[a][1] = c
                a = parents[a][0]
            while b != lca:
                parents[b][1] = c
                b = parents[b][0]

        elif query[0] == 2:
            a, b = query[1], query[2]
            # backup color, then delete a form parent of a
            # and move a to child of b
            # edges[parents[a]][a] = 0
            parents[a][0] = b

        else:
            a, b = query[1], query[2]
            # find lca node of a and b
            count = set()
            lca = get_lca(parents, a, b)
            while a != lca:
                count.add(parents[a][1])
                a = parents[a][0]
            while b != lca:
                count.add(parents[b][1])
                b = parents[b][0]
            print(len(count))


def main():
    n, k = read_list_int()
    quries = []
    for _ in range(k):
        quries.append(read_list_int())
    solution(n, k, quries)


if __name__ == '__main__':
    main()