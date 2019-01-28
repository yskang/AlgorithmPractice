# Title: 체스판 다시 칠하기
# Link: https://www.acmicpc.net/problem/1018

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_str = lambda: list(sys.stdin.readline().strip())

WHITE = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
BLACK = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

def check_board(x: int, y: int, board: list):
    white, black = 0, 0

    for yy in range(8):
        for xx in range(8):
            color = board[y+yy][x+xx]
            if WHITE[yy][xx] != color:
                white += 1
            if BLACK[yy][xx] != color:
                black += 1

    return min(white, black)


def solution(n: int, m: int, board: list):
    x, y = 0, 0
    count = []
    for y in range(n-7):
        for x in range(m-7):
            count.append(check_board(x, y, board))
    return min(count)


def main():
    n, m = read_list_int()
    board = []
    for _ in range(n):
        board.append(read_list_str())
    print(solution(n, m, board))


if __name__ == '__main__':
    main()