# Title: 효율적인 홍보
# Link: https://www.acmicpc.net/problem/1325

import sys
from collections import defaultdict


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def get_scc_iter(vertices, edges):
    identified = set()
    stack = []
    index = {}
    boundaries = []

    for v in vertices:
        if v not in index:
            to_do = [('VISIT', v)]
            while to_do:
                operation_type, v = to_do.pop()
                if operation_type == 'VISIT':
                    index[v] = len(stack)
                    stack.append(v)
                    boundaries.append(index[v])
                    to_do.append(('POSTVISIT', v))
                    to_do.extend(
                        reversed([('VISITEDGE', w) for w in edges[v]]))
                elif operation_type == 'VISITEDGE':
                    if v not in index:
                        to_do.append(('VISIT', v))
                    elif v not in identified:
                        while index[v] < boundaries[-1]:
                            boundaries.pop()
                else:
                    if boundaries[-1] == index[v]:
                        boundaries.pop()
                        scc = set(stack[index[v]:])
                        del stack[index[v]:]
                        identified.update(scc)
                        # print(scc)
                        yield scc


def solution(n: int, pairs, starts, pairs_rev) -> str:
    counts = defaultdict(lambda: set())
    nodes = [i for i in range(1, n+1)]
    new_node = n+1
    scc_map = defaultdict(lambda: None)

    all_scc = []
    for scc in get_scc_iter(nodes, pairs):
        if len(scc) > 1:
            all_scc.append(scc)

    del nodes

    for scc in all_scc:
        scc_map[new_node] = set(scc)
        outs = set()
        ins = set()
        for node in scc:
            outs.update(pairs[node])
            ins.update(pairs_rev[node])
        outs = outs.difference(scc)
        ins = ins.difference(scc)
        pairs[new_node].update(outs)

        for node in ins:
            pairs[node] = pairs[node].difference(scc)
            pairs[node].add(new_node)

        for node in outs:
            pairs_rev[node] = pairs_rev[node].difference(scc)
            pairs_rev[node].add(new_node)

        counts[new_node] = scc
        if len(ins) == 0:
            starts.add(new_node)
        new_node += 1

    temp = set()
    while True:
        for node in starts:
            for manto in pairs[node]:
                if len(counts[node]) == 0:
                    counts[node].add(node)
                if len(counts[manto]) == 0:
                    counts[manto].add(manto)
                counts[manto].update(counts[node])
                pairs_rev[manto].discard(node)
                if len(pairs_rev[manto]) == 0:
                    temp.add(manto)
        starts, temp = temp, set()
        if len(starts) == 0:
            break

    del pairs
    del pairs_rev
    del starts

    res = []

    counts_lens = defaultdict(lambda: 0)
    for node in counts:
        counts_lens[node] = len(counts[node])

    max_count = max(counts_lens.values())
    for node in counts_lens:
        if counts_lens[node] == max_count:
            res.append(node)

    del counts_lens

    ans = set()
    for r in res:
        if r in scc_map:
            for c in scc_map[r]:
                ans.add(c)
        else:
            ans.add(r)
    ans = sorted(ans)

    return ' '.join(map(str, ans))


def main():
    n, m = read_list_int()
    pairs = defaultdict(lambda: set())
    pairs_rev = defaultdict(lambda: set())
    starts = set([i for i in range(1, n+1)])

    for _ in range(m):
        manti, manto = read_list_int()
        pairs[manti].add(manto)
        pairs_rev[manto].add(manti)
        starts.discard(manto)
    print(solution(n, pairs, starts, pairs_rev))


if __name__ == '__main__':
    main()