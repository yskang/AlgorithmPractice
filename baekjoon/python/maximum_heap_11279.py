# Title: 최대 힙
# Link: https://www.acmicpc.net/problem/11279

import sys
from heapq import heappush, heappop

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(ops: list):
    mheap = []
    ans = []
    for op in ops:
        if op == 0:
            ans.append(-heappop(mheap) if mheap else 0)
        else:
            heappush(mheap, -op)
    return '\n'.join(map(str, ans))


def main():
    n = read_single_int()
    ops = []
    for _ in range(n):
        ops.append(read_single_int())
    print(solution(ops))


if __name__ == '__main__':
    main()