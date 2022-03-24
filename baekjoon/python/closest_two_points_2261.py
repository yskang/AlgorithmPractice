# Title: 가장 가까운 두 점
# Link: https://www.acmicpc.net/problem/2261

import sys
from collections import defaultdict
from bisect import bisect_left
import math


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
INF = 10**10


def solution(n: int, dots: list):
    d = INF
    dots = sorted(dots, key=lambda z: z[1])
    dot_list = defaultdict(lambda: [])
    for dot in dots:
        dot_list[dot[0]].append(dot[1])
        if len(dot_list[dot[0]]) > 1:
            d = min(d, (dot_list[dot[0]][-1]-dot_list[dot[0]][-2])**2)
    xs = sorted(dot_list.keys())

    for i in range(len(xs)):
        j = 1
        ys_a = dot_list[xs[i]]

        while i+j < len(xs) and (xs[i+j]-xs[i])**2 < d:
            ys_b = dot_list[xs[i+j]]
            diff = int(math.sqrt(d-(xs[i+j]-xs[i])**2))
            for y_a in ys_a:
                low = bisect_left(ys_b, y_a-diff)
                high = bisect_left(ys_b, y_a+diff)
                for y_b in ys_b[max(0, low): min(len(ys_b), high+1)]:
                    d = min(d, (xs[i]-xs[i+j])**2 + (y_a- y_b)**2)
            j += 1

    return d


def main():
    n = read_single_int()
    dots = []
    for _ in range(n):
        dots.append(read_list_int())
    print(solution(n, dots))


if __name__ == '__main__':
    main()