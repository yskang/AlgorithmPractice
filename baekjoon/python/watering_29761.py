# Title: 물 뿌리기
# Link: https://www.acmicpc.net/problem/29761

import sys
from collections import deque


offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, initial_x: int, row: int, col: int, height_map: list):
    water_map = [[0 for _ in range(n+1)] for _ in range(n+1)]
    water_map[row][col] = initial_x

    q = deque()
    q.append((col, row))
    qq = deque()
    # for same height, reduce water level
    while True:
        while q:
            pos_x, pos_y = q.popleft()

            current_height = height_map[pos_y][pos_x]
            current_water = water_map[pos_y][pos_x]

            if current_water <= 1:
                continue
            
            for offset_x, offset_y in offsets:
                next_x = pos_x + offset_x
                next_y = pos_y + offset_y

                if 0 < next_x <= n and 0 < next_y <= n:
                    next_height = height_map[next_y][next_x]
                    next_water = water_map[next_y][next_x]

                    if next_height < current_height:
                        if water_map[next_y][next_x] != initial_x:
                            water_map[next_y][next_x] = initial_x
                            qq.append((next_x, next_y))

                    elif next_height == current_height and next_water < current_water-1:
                        water_map[next_y][next_x] = current_water-1
                        q.append((next_x, next_y))
        if not qq:
            break
        q, qq = qq, q
    
    s = 0
    for row in water_map:
        # print(row, len(list(filter(lambda x: x > 0, row))))
        s += len(list(filter(lambda x: x > 0, row)))
    # print(s)
    # print('---------------')
    return s


def main():
    n, initital_x, x, y = read_list_int()
    height_map = [[]]
    for _ in range(n):
        height_map.append([0] + read_list_int())
    print(solution(n, initital_x, x, y, height_map))


if __name__ == '__main__':
    main()
