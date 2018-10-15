# Title: 쿼드트리
# Link: https://www.acmicpc.net/problem/1992

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_quadtree(image, start_x, start_y, N):
    base = image[start_y][start_x]
    all_same = True
    for y in range(start_y, start_y+N):
        for x in range(start_x, start_x+N):
            if image[y][x] != base:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        return base

    ul = get_quadtree(image, start_x, start_y, N//2)
    ur = get_quadtree(image, start_x+N//2, start_y, N//2)
    dl = get_quadtree(image, start_x, start_y+N//2, N//2)
    dr = get_quadtree(image, start_x+N//2, start_y+N//2, N//2)

    return '({}{}{}{})'.format(ul, ur, dl, dr)


if __name__ == '__main__':
    N = read_single_int()
    image = []
    for _ in range(N):
        image.append(sys.stdin.readline().strip())
    print(get_quadtree(image, 0, 0, N))