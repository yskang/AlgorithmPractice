# Title: 미로 탈출
# Link: https://www.acmicpc.net/problem/1473

import sys
from heapq import heappop, heappush

rotate = {
    'A': 'A',
    'B': 'B',
    'C': 'D',
    'D': 'C',
}


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_str() -> str:
    return sys.stdin.readline().strip()


def solution(n: int, m: int, maze: list) -> int:
    # print(n, m)
    # for row in maze:
    #     print(row)
    ans = 10**5
    visited = [[[[10**5 for _ in range(1 << m)] for _ in range(1 << n)] for _ in range(m)] for _ in range(n)]
    queue = []
    # time, r, c, change_row, change_col, prev_position(0: start, 1: from up, 2: from right, 3: from down, 4: from left)
    heappush(queue, (0, 0, 0, 0, 0, 0))
    visited[0][0][0][0] = 0

    t1, t2, xr, xc = 0, 0, 0, 0

    while queue:
        time, r, c, change_row, change_col, prev_position = heappop(queue)
        # staut of block when visited
        # already rotated state from previous position
        # rotate current block as change_row, change_col
        if r == n-1 and c == m-1:
            ans = min(ans, time)
            break

        if visited[r][c][change_row][change_col] < time:
            continue

        current_shape = maze[r][c]
        if change_row & (1 << r):
            current_shape = rotate[current_shape]
        if change_col & (1 << c):
            current_shape = rotate[current_shape]

        t1 = time + 1
        t2 = time + 2
        xr = change_row ^ (1 << r)
        xc = change_col ^ (1 << c)

        # case 1: move to right
        rr, cc = r, c + 1
        if cc < m and prev_position != 2:
            next_shape = maze[rr][cc]
            if change_row & (1 << rr):
                next_shape = rotate[next_shape]
            if change_col & (1 << cc):
                next_shape = rotate[next_shape]
            if current_shape == 'A' or current_shape == 'D':
                if next_shape == 'A':  # just move to right or rotate
                    if t1 < visited[rr][cc][change_row][change_col]:
                        visited[rr][cc][change_row][change_col] = t1
                        heappush(queue, ((t1, rr, cc, change_row, change_col, 4)))
                    if t2 < visited[rr][cc][xr][xc]:
                        visited[rr][cc][xr][xc] = t2
                        heappush(queue, ((t2, rr, cc, xr, xc, 4)))
                elif next_shape == 'D':  # just move to right
                    if t1 < visited[rr][cc][change_row][change_col]:
                        visited[rr][cc][change_row][change_col] = t1
                        heappush(queue, ((t1, rr, cc, change_row, change_col, 4)))
                elif next_shape == 'C':  # need to rotate
                    if t2 < visited[rr][cc][xr][xc]:
                        visited[rr][cc][xr][xc] = t2
                        heappush(queue, ((t2, rr, cc, xr, xc, 4)))

        # case 2: move to down
        rr, cc = r + 1, c
        if rr < n and prev_position != 3:
            next_shape = maze[rr][cc]
            if change_row & (1 << rr):
                next_shape = rotate[next_shape]
            if change_col & (1 << cc):
                next_shape = rotate[next_shape]
            if current_shape == 'A' or current_shape == 'C':
                if next_shape == 'A':
                    if t1 < visited[rr][cc][change_row][change_col]:
                        visited[rr][cc][change_row][change_col] = t1
                        heappush(queue, ((t1, rr, cc, change_row, change_col, 1)))
                    if t2 < visited[rr][cc][xr][xc]:
                        visited[rr][cc][xr][xc] = t2
                        heappush(queue, ((t2, rr, cc, xr, xc, 1)))
                elif next_shape == 'C':
                    if t1 < visited[rr][cc][change_row][change_col]:
                        visited[rr][cc][change_row][change_col] = t1
                        heappush(queue, ((t1, rr, cc, change_row, change_col, 1)))
                elif next_shape in 'D':
                    if t2 < visited[rr][cc][xr][xc]:
                        visited[rr][cc][xr][xc] = t2
                        heappush(queue, ((t2, rr, cc, xr, xc, 1)))

        # case 3: move to left
        rr, cc = r, c - 1
        if cc >= 0 and prev_position != 4:
            next_shape = maze[rr][cc]
            if change_row & (1 << rr):
                next_shape = rotate[next_shape]
            if change_col & (1 << cc):
                next_shape = rotate[next_shape]
            if current_shape == 'A' or current_shape == 'D':
                if next_shape == 'A':
                    if t1 < visited[rr][cc][change_row][change_col]:
                        visited[rr][cc][change_row][change_col] = t1
                        heappush(queue, ((t1, rr, cc, change_row, change_col, 2)))
                    if t2 < visited[rr][cc][xr][xc]:
                        heappush(queue, ((t2, rr, cc, xr, xc, 2)))
                elif next_shape == 'D':
                    if t1 < visited[rr][cc][change_row][change_col]:
                        visited[rr][cc][change_row][change_col] = t1
                        heappush(queue, ((t1, rr, cc, change_row, change_col, 2)))
                elif next_shape == 'C':
                    if t2 < visited[rr][cc][xr][xc]:
                        visited[rr][cc][xr][xc] = t2
                        heappush(queue, ((t2, rr, cc, xr, xc, 2)))

        # case 4: move to up
        rr, cc = r - 1, c
        if rr >= 0 and prev_position != 1:
            next_shape = maze[rr][cc]
            if change_row & (1 << rr):
                next_shape = rotate[next_shape]
            if change_col & (1 << cc):
                next_shape = rotate[next_shape]
            if current_shape == 'A' or current_shape == 'C':
                if next_shape == 'A':
                    if t1 < visited[rr][cc][change_row][change_col]:
                        visited[rr][cc][change_row][change_col] = t1
                        heappush(queue, ((t1, rr, cc, change_row, change_col, 3)))
                    if t2 < visited[rr][cc][xr][xc]:
                        visited[rr][cc][xr][xc] = t2
                        heappush(queue, ((t2, rr, cc, xr, xc, 3)))
                elif next_shape == 'C':
                    if t1 < visited[rr][cc][change_row][change_col]:
                        visited[rr][cc][change_row][change_col] = t1
                        heappush(queue, ((t1, rr, cc, change_row, change_col, 3)))
                elif next_shape == 'D':
                    if t2 < visited[rr][cc][xr][xc]:
                        visited[rr][cc][xr][xc] = t2
                        heappush(queue, ((t2, rr, cc, xr, xc, 3)))

    return ans if ans != 10**5 else -1


def main():
    n, m = read_list_int()
    maze = []
    for _ in range(n):
        maze.append(read_single_str())
    print(solution(n, m, maze))


if __name__ == '__main__':
    main()