# Title: 팬이에요
# Link: https://www.acmicpc.net/problem/16115

import sys
import math
import collections


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def distance2(a: int, b: int):
    return pow(a, 2) + pow(b, 2)


def get_angle(a: int, b: int):
    d = math.degrees(math.atan2(b, a))
    if d < 0:
        d = 360 + d
    return d


def solution(n: int, coords: list):
    ls = collections.defaultdict(lambda: [])

    for (x, y) in coords:
        ls[distance2(x, y)].append((x, y))
    
    sorted_ls = sorted(ls.keys(), reverse=True)
    dots = ls[sorted_ls[0]]
    angles = []
    for dot in dots:
        angles.append(get_angle(*dot))
    angles = sorted(angles)
    max_diff_angle = 0
    prev_angle = angles[0]
    for angle in angles[1:]:
        max_diff_angle = max(angle - prev_angle, max_diff_angle)
        prev_angle = angle
    max_diff_angle = max(max_diff_angle, 360 - angles[-1] + angles[0])
    return max_diff_angle


def main():
    n = read_single_int()
    coords = []
    for _ in range(n):
        coords.append(read_list_int())
    print(solution(n, coords))


if __name__ == '__main__':
    main()