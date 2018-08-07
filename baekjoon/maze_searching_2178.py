# Title: 미로 탑색
# Link: https://www.acmicpc.net/problem/2178

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def move_next(maze, pos, step, width, height):
    positions = []
    offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for offset in offsets:
        xx = pos[0] + offset[0]
        yy = pos[1] + offset[1]
        if 0 <= xx < width and 0 <= yy < height and maze[yy][xx] == 1:
            maze[yy][xx] = step + 1
            positions.append((xx, yy))
    return positions


def get_minimum_move(maze, N, M):
    step = 0
    next_positions = [(0, 0)]
    temp = set()
    while True:
        step += 1
        for pos in next_positions:
            next_positions = move_next(maze, pos, step, M, N)
            for nexts in next_positions:
                temp.add(nexts)
        if maze[N-1][M-1] != 1:
            return maze[N-1][M-1]
        next_positions = list(temp)
        temp = set()


if __name__ == '__main__':
    N, M = read_list_int()
    maze = []
    for _ in range(N):
        maze.append(list(map(int, sys.stdin.readline().strip())))
    print(get_minimum_move(maze, N, M))