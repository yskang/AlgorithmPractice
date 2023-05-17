# Title: 미로 탈출하기
# Link: https://www.acmicpc.net/problem/17090

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_str() -> str:
    return sys.stdin.readline().strip()


def dfs(x: int, y: int, maze: list, path: set, possibles: list, is_escape: list):
    if (x, y) in path:
        is_escape[0] = False
        return
    path.add((x, y))
    if possibles[y][x] == 1:
        return
    if maze[y][x] == 'U':
        xx, yy = x, y-1
        if yy < 0:
            return
        dfs(xx, yy, maze, path, possibles, is_escape)
    elif maze[y][x] == 'R':
        xx, yy = x+1, y
        if xx >= len(maze[0]):
            return
        dfs(xx, yy, maze, path, possibles, is_escape)
    elif maze[y][x] == 'D':
        xx, yy = x, y+1
        if yy >= len(maze):
            return
        dfs(xx, yy, maze, path, possibles, is_escape)
    elif maze[y][x] == 'L':
        xx, yy = x-1, y
        if xx < 0:
            return
        dfs(xx, yy, maze, path, possibles, is_escape)


def solution(n: int, m: int, maze: list):
    possibles = [[0 for _ in range(m)] for _ in range(n)]

    for y in range(n):
        for x in range(m):
            path = set()
            is_escape = [True]
            dfs(x, y, maze, path, possibles, is_escape)
            if is_escape[0]:
                for xx, yy in path:
                    possibles[yy][xx] = 1

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