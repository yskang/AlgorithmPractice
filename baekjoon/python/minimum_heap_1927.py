# Title: 최소 힙
# Link: https://www.acmicpc.net/problem/1927

import sys
from heapq import heappush, heappop

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(ops: list):
    heap = []
    for op in ops:
        if op == 0:
            print(heappop(heap) if heap else 0)
        else:
            heappush(heap, op)


def main():
    n = read_single_int()
    ops = []
    for _ in range(n):
        ops.append(read_single_int())
    solution(ops)


if __name__ == '__main__':
    main()