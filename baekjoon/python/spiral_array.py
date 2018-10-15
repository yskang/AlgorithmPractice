import sys


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def mark_number(number, x, y, w, h, come_from, spiral, count):
    if count >= 3:
        return
    if x < 0 or y < 0 or y >= h or x >= w or spiral[y][x] != '-':
        if come_from == 'left':
            come_from = 'up'
            x -= 1
            y += 1
        elif come_from == 'right':
            come_from = 'down'
            x += 1
            y -= 1
        elif come_from == 'up':
            come_from = 'right'
            y -= 1
            x -= 1
        elif come_from == 'down':
            come_from = 'left'
            y += 1
            x += 1
        mark_number(number, x, y, w, h, come_from, spiral, count+1)
    else:
        spiral[y][x] = number
        if come_from == 'left':
            x += 1
        elif come_from == 'right':
            x -= 1
        elif come_from == 'up':
            y += 1
        elif come_from == 'down':
            y -= 1
        mark_number(number+1, x, y, w, h, come_from, spiral, 0)


def get_spiral(w, h, blocks):
    spiral = [['-' for _ in range(w)] for _ in range(h)]
    for (x, y) in blocks:
        spiral[y][x] = 'X'

    mark_number(0, 0, 0, w, h, 'left', spiral, 0)

    return spiral


if __name__ == '__main__':
    w, h = read_list_int()
    n = read_single_int()
    blocks = []
    for _ in range(n):
        x, y = read_list_int()
        blocks.append((x, y))
    for row in get_spiral(w, h, blocks):
        print(row)