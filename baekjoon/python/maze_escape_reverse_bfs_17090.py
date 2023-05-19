# Title: 미로 탈출하기
# Link: https://www.acmicpc.net/problem/17090

import sys
from collections import deque


#  [x, y], up, down, left, right
offsets = [[0, -1, 'D'], [0, 1, 'U'], [-1, 0, 'R'], [1, 0, 'L']]


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_str() -> str:
    return sys.stdin.readline().strip()


def bfs(x: int, y: int, maze: list, possibles: list):
    if possibles[y][x] == 1:
        return
    possibles[y][x] = 1

    q = deque()
    q.append((x, y))

    while q:
        xx, yy = q.popleft()
        for dx, dy, dir in offsets:
            xxx, yyy = xx + dx, yy + dy
            if 0 <= xxx < len(maze[0]) and 0 <= yyy < len(maze) and maze[yyy][xxx] == dir:
                if possibles[yyy][xxx] == 0:
                    possibles[yyy][xxx] = 1
                    q.append((xxx, yyy))


def solution(n: int, m: int, maze: list):
    possibles = [[0 for _ in range(m)] for _ in range(n)]

    xs = [i for i in range(m)] + [i for i in range(m)] + [0 for _ in range(n)] + [m-1 for _ in range(n)]
    ys = [0 for _ in range(m)] + [n-1 for _ in range(m)] + [i for i in range(n)] + [i for i in range(n)]
    zs = ['U' for _ in range(m)] + ['D' for _ in range(m)] + ['L' for _ in range(n)] + ['R' for _ in range(n)]

    xys = zip(xs, ys, zs)

    for x, y, z in xys:
        if maze[y][x] == z:
            bfs(x, y, maze, possibles)

    ans = 0
    for line in possibles:
        ans += sum(line)
    return ans


def main():
    n, m = read_list_int()
    maze = []
    for _ in range(n):
        maze.append(list(read_single_str()))
    print(solution(n, m, maze))


if __name__ == '__main__':
    main()
