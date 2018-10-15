# Title: 소용돌이 예쁘게 출력하기
# Link: https://www.acmicpc.net/problem/1022

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_number(x, y, ends):
    num = 1
    if x == y == 0:
        return num
    (big, small) = (x, y) if abs(x) >= abs(y) else (y, x)
    corners = []

    width = abs(big)*2+1

    corners.append(ends[width - 2] + width - 1)
    for _ in range(3):
        corners.append(corners[-1] + width - 1)

    if x == y and x > 0:
        return corners[3]
    elif x == y and x < 0:
        return corners[1]
    elif x + y == 0 and x < 0:
        return corners[2]
    elif x + y == 0 and x > 0:
        return corners[0]

    if x == big and x > 0:
        num = corners[0] - (x+y)
    elif x == big and x < 0:
        num = corners[2] + (x+y)
    elif y == big and y > 0:
        num = corners[3] - (y-x)
    else:
        num = corners[1] + (y-x)

    return num


def get_spiral(y1, x1, y2, x2, ends):
    spiral = []
    spiral_str = []
    max_lengths = 0
    for y in range(y1, y2+1):
        row = []
        for i, x in enumerate(range(x1, x2+1)):
            num = get_number(x, y, ends)
            row.append(num)
            max_lengths = max(max_lengths, len(str(num)))
        spiral.append(row)
    for row in spiral:
        row_str = []
        for i, n in enumerate(row):
            f_str = '{0:' + str(max_lengths) + 'd}'
            row_str.append(f_str.format(row[i]))
        spiral_str.append(' '.join(row_str))
    return '\n'.join(spiral_str)


if __name__ == '__main__':
    ends = [0] * 10002
    ends[1] = 1
    for w in range(3, 10002, 2):
        ends[w] = ends[w - 2] + w * 2 + (w - 2) * 2
    r1, c1, r2, c2 = read_list_int()
    print(get_spiral(r1, c1, r2, c2, ends))
