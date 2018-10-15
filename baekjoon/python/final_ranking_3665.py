# Title: 최종 순위
# Link: https://www.acmicpc.net/problem/3665

import sys

import heapq

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_final_ranks(old_ranks, changes, n, m):
    hq = []
    nodes = [[] for _ in range(n+1)]
    indegrees = [0 for _ in range(n+1)]

    for i, node in enumerate(old_ranks):
        nodes[node] = old_ranks[i+1:]
        indegrees[node] = i

    for (a, b) in changes:
        if b in nodes[a]:
            nodes[a].remove(b)
            nodes[b].append(a)
            indegrees[a] += 1
            indegrees[b] -= 1
        else:
            nodes[b].remove(a)
            nodes[a].append(b)
            indegrees[b] += 1
            indegrees[a] -= 1

    for node, indegree in enumerate(indegrees[1:], 1):
        if indegree == 0:
            heapq.heappush(hq, node)

    ans = []
    while len(hq) > 0:
        poped = heapq.heappop(hq)
        ans.append(poped)
        for node in nodes[poped]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                heapq.heappush(hq, node)

    if len(ans) != n:
        return 'IMPOSSIBLE'
    return ' '.join(map(str, ans))


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        n = read_single_int()
        ts = read_list_int()
        m = read_single_int()
        changes = []
        for _ in range(m):
            a, b = read_list_int()
            changes.append((a, b))
        print(get_final_ranks(ts, changes, n, m))