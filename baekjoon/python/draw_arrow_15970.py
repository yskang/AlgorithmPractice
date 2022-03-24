# Title: 화살표 그리기
# Link: https://www.acmicpc.net/problem/15970

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, dots: list):
    ans = 0
    for color in dots:
        positions = sorted(dots[color])
        ans += positions[1] - positions[0]
        ans += positions[-1] - positions[-2]
        for i, pos in enumerate(positions[1:-1], 1):
            ans += min(positions[i+1]-pos, pos-positions[i-1])
    return ans


def main():
    n = read_single_int()
    dots = defaultdict(lambda: [])
    for _ in range(n):
        x, y = read_list_int()
        dots[y].append(x)
    print(solution(n, dots))


if __name__ == '__main__':
    main()