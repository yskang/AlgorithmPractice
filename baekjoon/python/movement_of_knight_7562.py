# Title: 나이트의 이동
# Link: https://www.acmicpc.net/problem/7562

import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


offsets = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]


def is_valid_position(position, l):
    if 0 <= position[0] < l and 0 <= position[1] < l:
        return True
    return False


def solution(l: int, knight: tuple, goal: tuple):
    if knight == goal:
        return 0

    board = [[-1 for _ in range(l)] for _ in range(l)]
    board[knight[1]][knight[0]] = 0

    q = deque()
    q.append((knight, 0))

    while True:
        current_position, t = q.popleft()

        for offset in offsets:
            next_position = (current_position[0] + offset[0], current_position[1] + offset[1])
            if is_valid_position(next_position, l) and board[next_position[1]][next_position[0]] == -1:
                q.append((next_position, t+1))
                board[next_position[1]][next_position[0]] = t+1
                if next_position == goal:
                    return t+1
            

def main():
    t = read_single_int()
    for _ in range(t):
        l = read_single_int()
        x, y = read_list_int()
        knight = (x, y)
        v, w = read_list_int()
        goal = (v, w)
        print(solution(l, knight, goal))


if __name__ == '__main__':
    main()