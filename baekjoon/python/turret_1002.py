# Title: 터렛
# Link: https://www.acmicpc.net/problem/1002

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def dist2(x: int, y: int, xx: int, yy: int):
    return (x-xx)**2 + (y-yy)**2


def solution(x: int, y: int, r: int, xx: int, yy: int, rr: int):
    d = dist2(x, y, xx, yy)
    if x==xx and y==yy:
        if r == rr:
            return -1
        return 0
    if (r - rr)**2 == d:
        return 1
    if (d < r*r and d < (r-rr)**2) or (d<rr*rr and d<(rr-r)**2):
        return 0
    if d > (r+rr)**2:
        return 0
    if d == (r+rr)**2:
        return 1
    return 2


def main():
    t = read_single_int()
    for _ in range(t):
        x, y, r, xx, yy, rr = read_list_int()
        print(solution(x, y, r, xx, yy, rr))


if __name__ == '__main__':
    main()