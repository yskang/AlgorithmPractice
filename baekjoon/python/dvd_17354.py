# Title: DVD
# Link: https://www.acmicpc.net/problem/17354

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def is_corner(tv_w, tv_h, box_w, box_h, x, y):
    if x == 0 and y == 0:
        return True
    elif y == 0 and x + box_w == tv_w:
        return True
    elif x == 0 and y + box_h == tv_h:
        return True
    elif x + box_w == tv_w and y + box_h == tv_h:
        return True
    return False


def get_touch(tv_w, tv_h, box_w, box_h, x, y, acc_x, acc_y):
    top = y
    left = x
    right = tv_w-(x+box_w)
    bottom = tv_h-(y+box_h)
    time = 0
    h_time, v_time = 0, 0

    d_top, d_bottom, d_left, d_right = False, False, False, False

    if acc_x == -1:
        h_time = left
        d_left = True
    elif acc_x == 1:
        h_time = right
        d_right = True
    if acc_y == -1:
        v_time = top
        d_top = True
    elif acc_y == 1:
        v_time = bottom
        d_bottom = True

    if h_time == v_time:
        time = h_time
        acc_x = -acc_x
        acc_y = -acc_y
    elif h_time < v_time:
        time = h_time
        acc_x = -acc_x
    else:
        time = v_time
        acc_y = -acc_y

    if d_left:
        x = x - time
    elif d_right:
        x = x + time
    if d_top:
        y = y - time
    elif d_bottom:
        y = y + time

    return time, x, y, acc_x, acc_y


def solution(box_w: int, box_h: int, tv_width: int, tv_height: int, x: int, y: int, acc_x: int, acc_y: int):
    if is_corner(tv_width, tv_height, box_w, box_h, x, y):
        return 0
    time = 0
    i_x, i_y, i_acc_x, i_acc_y = -1, -1, -1, -1
    first = True
    while True:
        t, x, y, acc_x, acc_y = get_touch(tv_width, tv_height, box_w, box_h, x, y, acc_x, acc_y)
        if first:
            first = False
            i_x, i_y, i_acc_x, i_acc_y = x, y, acc_x, acc_y
        else:
            if i_x == x and i_y == y and i_acc_x == acc_x and i_acc_y == acc_y:
                return -1

        time += t
        if is_corner(tv_width, tv_height, box_w, box_h, x, y):
            return time


def main():
    tv_width, tv_height, box_w, box_h = read_list_int()
    x, y = read_list_int()
    acc_x, acc_y = read_list_int()
    print(solution(tv_width, tv_height, box_w, box_h, x, y, acc_x, acc_y))


if __name__ == '__main__':
    main()