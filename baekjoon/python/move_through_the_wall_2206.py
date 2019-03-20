# Title: 벽 부수고 이동하기
# Link: https://www.acmicpc.net/problem/2206

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_str = lambda: list(sys.stdin.readline().strip())


def solution(n: int, m: int, game_map: list):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visits = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(n)]

    queue = deque()
    queue.append((0, 0, False, 1))
    visits[0][0][0] = 1

    while queue:
        x, y, broken, step = queue.popleft()
        
        for move in moves:
            xx, yy = x + move[0], y + move[1]
            if 0 <= xx < m and 0 <= yy < n:
                if broken:
                    if game_map[yy][xx] == '0' and visits[yy][xx][1] == -1:
                        visits[yy][xx][1] = step+1
                        queue.append((xx, yy, True, step+1))
                elif not broken:
                    if game_map[yy][xx] == '0' and visits[yy][xx][0] == -1:
                        visits[yy][xx][0] = step+1
                        queue.append((xx, yy, False, step+1))
                    elif game_map[yy][xx] == '1' and visits[yy][xx][1] == -1:
                        visits[yy][xx][1] = step+1
                        queue.append((xx, yy, True, step+1))

    return max(visits[n-1][m-1]) if -1 in visits[n-1][m-1] else min(visits[n-1][m-1])


def main():
    N, M = read_list_int()
    game_map = []
    for _ in range(N):
        game_map.append(read_list_str())
    print(solution(N, M, game_map))


if __name__ == '__main__':
    main()