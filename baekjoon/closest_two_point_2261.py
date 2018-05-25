# Title: 가장 가까운 두 점
# Link: https://www.acmicpc.net/problem/2261
import math
import sys

from collections import namedtuple

import bisect

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def distance_square(a, b):
    return (a.x-b.x)**2 + (a.y-b.y)**2


def min_distance_divide_and_conquer(points, n):
    if n == 2:
        return distance_square(*points)
    elif n == 3:
        return min(distance_square(*points[:2]), distance_square(*points[1:]), distance_square(points[0], points[2]))

    line = (points[n//2-1].x + points[n//2].x)//2
    d = min(min_distance_divide_and_conquer(points[:n // 2], n // 2), min_distance_divide_and_conquer(points[n // 2:], n - n // 2))

    points_in_middle = []

    for point in points:
        t = line - point.x
        if t**2 <= d:
            points_in_middle.append(point)

    points_in_middle = sorted(points_in_middle, key=lambda p: p.y)

    for i, first_point in enumerate(points_in_middle):
        for second_point in points_in_middle[i+1:i+7]:
            d = min(d, distance_square(first_point, second_point))

    return d


def min_distance_sweep_line(points):
    ds = distance_square(*points[:2])
    d = math.sqrt(ds)
    xs, _ = zip(*points)
    for i, point in enumerate(points[2:], 2):
        s = bisect.bisect_left(xs, point.x-d)
        candidates = points[s:i]
        candidates = sorted(candidates, key=lambda p: p.y)
        _, ys = zip(*candidates)
        start = bisect.bisect_left(ys, point.y - d)
        end = bisect.bisect_right(ys, point.y + d)
        for c in candidates[start:end]:
            ds = min(distance_square(c, point), ds)
    return ds


if __name__ == '__main__':
    n = read_single_int()
    points = []
    Point = namedtuple('Point', 'x y')
    for _ in range(n):
        x, y = read_list_int()
        points.append(Point(x, y))
    points = sorted(points, key=lambda p: p.x)
    # print(min_distance_divide_and_conquer(points, n))
    print(min_distance_sweep_line(points))