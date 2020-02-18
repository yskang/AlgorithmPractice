# Title: 지금 만나러 갑니다
# Link: https://www.acmicpc.net/problem/18235

import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def bfs(n: int, b: int):
    queue = deque()
    queue.append((b, 0))

    positions = set()

    yield

    t = 0
    while queue:
        ori, time = queue.popleft()
        positions.discard((ori, time))

        if t != time:
            t += 1
            positions.add((ori, time))
            yield positions
            positions.discard((ori, time))

        p = ori - pow(2, time)
        if 0 < p:
            queue.append((p, time+1))
            positions.add((p, time+1))
        p = ori + pow(2, time)
        if p <= n:
            queue.append((p, time+1))
            positions.add((p, time+1))

    yield -1


def solution(n: int, a: int, b: int):
    queue = deque()
    queue.append((a, 0))

    bfs_co = bfs(n, b)
    next(bfs_co)

    t = 0
    while queue:
        ori, time = queue.popleft()

        if t != time:
            t += 1
            ori_b = next(bfs_co)
            if ori_b == -1:
                return -1
            if ((ori, time)) in ori_b:
                return time
            for ori_a in queue:
                if ori_a in ori_b:
                    return time

        p = ori - pow(2, time)
        if p > 0:
            queue.append((p, time+1))
        p = ori + pow(2, time)
        if p <= n:
            queue.append((p, time+1))

    return -1


def main():
    n, a, b = read_list_int()
    print(solution(n, a, b))


if __name__ == '__main__':
    main()