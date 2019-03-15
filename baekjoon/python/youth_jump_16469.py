# Title: 소년점프
# Link: https://www.acmicpc.net/problem/16469

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_str = lambda: sys.stdin.readline().strip()


def mark(i: int, e_map: list, r: int, c: int, maze: list, queue: deque):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    x, y = queue.popleft()
    num = e_map[y][x][i]

    for move in moves:
        xx, yy = x+move[0], y+move[1]
        if (0 <= xx < c) and (0 <= yy < r) and (e_map[yy][xx][i] == -1) and (maze[yy][xx] != 1):
            queue.append((xx, yy))
            e_map[yy][xx][i] = num+1
    

def solution(r: int, c: int, maze: list, enermies: list):
    e_map = [[[-1, -1, -1] for _ in range(c)] for _ in range(r)]
    for i, (y, x) in enumerate(enermies):
        x, y = x-1, y-1
        queue = deque()
        queue.append((x, y))
        e_map[y][x][i] = 0
        while queue:
            mark(i, e_map, r, c, maze, queue)

    min_pos_num = 0
    min_move = 99999999999999
    for row in e_map:
        for e in row:
            if -1 not in e:
                move = max(e)
                if min_move > move:
                    min_move = move
                    min_pos_num = 1
                elif min_move == move:
                    min_pos_num += 1

    if min_pos_num == 0:
        return -1
    return '{}\n{}'.format(min_move, min_pos_num)


def main():
    r, c = read_list_int()
    maze = []
    for _ in range(r):
        maze.append(list(map(int, list(read_single_str()))))
    enemies = []
    enemies.append(read_list_int())
    enemies.append(read_list_int())
    enemies.append(read_list_int())
    print(solution(r, c, maze, enemies))


if __name__ == '__main__':
    main()