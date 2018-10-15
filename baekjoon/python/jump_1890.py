# Title: 점프
# Link: https://www.acmicpc.net/problem/1890

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def update_count(count_table, x, y, board):
    i = 1
    u = 0
    while y - i >= 0:
        if board[y-i][x] == i:
            u += count_table[y-i][x]
        i += 1
    i = 1
    l = 0
    while x - i >= 0:
        if board[y][x-i] == i:
            l += count_table[y][x-i]
        i += 1

    count_table[y][x] = u + l


def get_minimum_step(board, N):
    count_table = [[0] * N for _ in range(N)]
    count_table[0][0] = 1
    start = 1
    while start < N:
        x = start
        y = 0
        while x >= 0 and y < N:
            update_count(count_table, x, y, board)
            x -= 1
            y += 1
        start += 1
    start = 1

    while start < N:
        x = N-1
        y = start
        while x >= 0 and y < N:
            update_count(count_table, x, y, board)
            x -= 1
            y += 1
        start += 1
    return count_table[N-1][N-1]


if __name__ == '__main__':
    N = read_single_int()
    board = []
    for _ in range(N):
        board.append(read_list_int())
    print(get_minimum_step(board, N))