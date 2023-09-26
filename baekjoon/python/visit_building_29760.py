# Title: 건물 방문하기
# Link: https://www.acmicpc.net/problem/29760

import sys


INF = 10**10


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def get_next_floor(building: list, current: int):
    for i in range(current+1, len(building)):
        if building[i]:
            return (i, building[i])
    return None, None


def solution(n: int, h: int, w: int, building: list[list]):
    for floor in building:
        floor.sort()

    current = [0, 0]

    prev_floor = []
    current_height = 0
    current_height, floor = get_next_floor(building, current_height)

    prev = [INF, floor[-1]-1 + (current_height-1) * 100]

    while True:
        prev_floor, floor = floor, prev_floor
        prev_height = current_height
        current_height, floor = get_next_floor(building, current_height)
        if not floor:
            break
        floor_length = floor[-1] - floor[0]
        dist_height = current_height - prev_height

        from_left = abs(prev_floor[0] - floor[-1]) + prev[0]
        form_right = abs(prev_floor[-1] - floor[-1]) + prev[1]
        current[0] = min(from_left, form_right) + dist_height * 100 + floor_length

        from_left = abs(prev_floor[0] - floor[0]) + prev[0]
        from_right = abs(prev_floor[-1] - floor[0]) + prev[1]
        current[1] = min(from_left, from_right) + dist_height * 100 + floor_length

        prev, current = current, prev

    return min(prev)


def main():
    n, h, w = read_list_int()
    building = [[] for _ in range(h+1)]
    for _ in range(n):
        x, y = read_list_int()
        building[x].append(y)

    print(solution(n, h, w, building))


if __name__ == '__main__':
    main()