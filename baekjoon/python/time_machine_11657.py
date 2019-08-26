# Title: 타임머신
# Link: https://www.acmicpc.net/problem/11657
import sys
from types import SimpleNamespace

sys.setrecursionlimit(10 ** 6)

INF = 999999999999999

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, m: int, nodes: list):
    times = [INF for _ in range(n+1)]
    times[1] = 0
    starts = [1]
    for k in range(n+1):
        updated = []
        for start in starts:
            for child, time in nodes[start]:
                if times[child] > time+times[start]:
                    times[child] = time+times[start]
                    updated.append(child)
        if k == n and updated != []:
            print(-1)
            return
        starts, updated = updated, start
    for t in times[2:]:
        print(-1) if t == INF else print(t)


def main():
    n, m = read_list_int()
    nodes = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = read_list_int()
        nodes[a].append((b, c))
    solution(n, m, nodes)


if __name__ == '__main__':
    main()