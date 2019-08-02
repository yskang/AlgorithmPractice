# Title: 달팽이
# Link: https://www.acmicpc.net/problem/1913

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def is_corner(x: int, y: int, n: int):
    if x+y == n-1:
        return True
    elif x >= n//2 and y >= n//2 and x == y:
        return True
    elif x < n//2 and y < n//2 and x-y==1:
        return True
    return False


def solution(n: int, num: int):
    ans = []
    snail = [[0 for _ in range(n)] for _ in range(n)]

    x, y = n//2, n//2
    snail[y][x] = 1
    y -= 1
    snail[y][x] = 2
    c = 2
    offsets = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    if num == 1:
        ans = [n//2+1, n//2+1]
    elif num == 2:
        ans = [n//2, n//2+1]

    while True:
        c += 1

        xx, yy = offsets[0]
        x += xx
        y += yy

        if 0 <= x < n and 0 <= y < n:
            snail[y][x] = c

            if c == num:
                ans = [y+1, x+1]

            if is_corner(x, y, n):
                offsets.rotate(-1)
        else:
            break
                
    for row in snail:
        print(*row)
    print(*ans)


def main():
    n = read_single_int()
    num = read_single_int()
    solution(n, num)


if __name__ == '__main__':
    main()