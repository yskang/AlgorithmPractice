# Title: 지금 만나러 갑니다
# Link: https://www.acmicpc.net/problem/18235

import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def bfs(n: int, b: int):
    queue = deque()
    queue.append((b, 0))

    pos = [0 for _ in range(n+1)]

    t = 0
    while queue:
        ori, time = queue.popleft()

        if t != time:
            t += 1
            pos[ori] = time
            yield pos

        offset = pow(2, time)
        p = ori - offset
        if 0 < p:
            queue.append((p, time+1))
            pos[p] = time+1
        p = ori + offset
        if p <= n:
            queue.append((p, time+1))
            pos[p] = time+1

    yield -1


def solution(n: int, a: int, b: int):
    queue = deque()
    queue.append((a, 0))

    bfs_co = bfs(n, b)
    ori_b = next(bfs_co)

    t = 0
    while queue:
        ori, time = queue.popleft()

        if time != t:
            t += 1
            ori_b = next(bfs_co)
            if ori_b == -1:
                return -1

        offset = pow(2, time)
        p = ori - offset
        if p > 0:
            queue.append((p, time+1))
            if ori_b[p] == time+1:
                return time+1
        p = ori + offset
        if p <= n:
            queue.append((p, time+1))
            if ori_b[p] == time+1:
                return time+1

    return -1


def main():
    n, a, b = read_list_int()
    print(solution(n, a, b))


if __name__ == '__main__':
    main()