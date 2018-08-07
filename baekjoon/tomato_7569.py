# Title: 토마토
# Link: https://www.acmicpc.net/problem/7569

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def update_tomatoes_around(boxes, x, y, z, day, width, height, depth):
    updated = []
    offsets = [(-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    for offset in offsets:
        xx = x + offset[0]
        yy = y + offset[1]
        zz = z + offset[2]
        if 0 <= xx < width and 0 <= yy < height and 0 <= zz < depth and boxes[zz][yy][xx] == 0:
            boxes[zz][yy][xx] = day + 1
            updated.append((xx, yy, zz))
    return updated


def get_minimum_day(boxes, width, height, depth):
    day = 0
    last_tomatoes = []
    changed = set()
    for z, box in enumerate(boxes):
        for y, row in enumerate(box):
            for x, tomato in enumerate(row):
                if tomato == 1:
                    last_tomatoes.append((x, y, z))

    while True:
        day += 1
        for (x, y, z) in last_tomatoes:
            updates = update_tomatoes_around(boxes, x, y, z, day, width, height, depth)
            for update in updates:
                changed.add(update)

        if len(changed) == 0:
            break
        last_tomatoes = list(changed)
        changed = set()

    for box in boxes:
        for row in box:
            if 0 in row:
                return -1

    return day - 1


if __name__ == '__main__':
    M, N, H = read_list_int()
    box = []
    boxes = []
    for _ in range(H):
        for _ in range(N):
            box.append(read_list_int())
        boxes.append(box)
        box = []
    print(get_minimum_day(boxes, M, N, H))