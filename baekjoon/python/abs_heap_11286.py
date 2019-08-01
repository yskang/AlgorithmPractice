# Title: 절대값 힙
# Link: https://www.acmicpc.net/problem/11286

import sys
from heapq import heappop, heappush


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(ops: list):
    q = []
    for op in ops:
        if op == 0:
            print(heappop(q)[1] if q else 0)
        else:
            heappush(q, (abs(op), op))


def main():
    n = read_single_int()
    ops = []
    for _ in range(n):
        ops.append(read_single_int())
    solution(ops)


if __name__ == '__main__':
    main()