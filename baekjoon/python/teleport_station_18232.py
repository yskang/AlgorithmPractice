# Title: 텔레포트 정거장
# Link: https://www.acmicpc.net/problem/18232

import sys
from collections import deque, defaultdict


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, s: int, e: int, stations: list):
    visited = defaultdict(lambda: False)
    visited[0] = True
    visited[n+1] = True
    queue = deque()
    queue.append((s, 0))
    visited[s] = True

    while queue:
        station, time = queue.popleft()
        for child in stations[station]:
            if not visited[child]:
                queue.append((child, time+1))
                visited[child] = True
                if child == e:
                    return time+1


def main():
    n, m = read_list_int()
    s, e = read_list_int()
    stations = [[i-1, i+1] for i in range(n+1)]
    for _ in range(m):
        x, y = read_list_int()
        stations[x].append(y)
        stations[y].append(x)

    print(solution(n, m, s, e, stations))


if __name__ == '__main__':
    main()