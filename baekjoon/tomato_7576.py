# Title: 토마토
# Link: https://www.acmicpc.net/problem/7576

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def update_tomatoes_around(box, x, y, day, width, height):
    updated = []
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for offset in offsets:
        xx = x + offset[0]
        yy = y + offset[1]
        if 0 <= xx < width and 0 <= yy < height and box[yy][xx] == 0:
            box[yy][xx] = day+1
            updated.append((xx, yy))
    return updated


def get_minimum_day(box, width, height):
    day = 0
    last_tomatoes = []
    changed = set()
    for y, row in enumerate(box):
        for x, tomato in enumerate(row):
            if tomato == 1:
                last_tomatoes.append((x, y))

    while True:
        day += 1
        for (x, y) in last_tomatoes:
            updates = update_tomatoes_around(box, x, y, day, width, height)
            for update in updates:
                changed.add(update)

        if len(changed) == 0:
            break
        last_tomatoes = list(changed)
        changed = set()

    for row in box:
        if 0 in row:
            return -1

    return day - 1


if __name__ == '__main__':
    M, N = read_list_int()
    box = []
    for _ in range(N):
        box.append(read_list_int())
    print(get_minimum_day(box, M, N))