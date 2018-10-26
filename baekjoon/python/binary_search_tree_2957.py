# Title: 이진 탐색 트리
# Link: https://www.acmicpc.net/problem/2957

import sys
import bisect
import collections
import heapq

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(size: int, ns: list):
    prev = 0
    depths = []
    heapq.heappush(depths, 0)
    heapq.heappush(depths, size+1)
    depth_map = collections.defaultdict(lambda: -1)

    for n in ns:
        heapq.heappush(depths, n)
        pos = bisect.bisect_left(depths, n)
        depth_map[n] = max(depth_map[depths[pos-1]], depth_map[depths[pos+1]]) + 1
        prev += depth_map[n]
        print(prev)
        print(depths)
        print(depth_map)


def main():
    n = read_single_int()
    ns = []
    for _ in range(n):
        ns.append(read_single_int())
    solution(n, ns)


if __name__ == '__main__':
    main()