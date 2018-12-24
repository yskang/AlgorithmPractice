# Title: Cherrypick
# Link: https://www.acmicpc.net/problem/16119

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_max(x: int, y: int, w: int, cs: list):
    ms = []
    for i in range(w):
        ms.append(max(cs[y+i][x:x+w]))
    return max(ms)


def update(v: int, x: int, y: int, w: int, vs: list):
    for i in range(w):
        for j in range(w):
            vs[y+i][x+j] = max(vs[y+i][x+j], v)


def solution(n: int, cs: list, vs: list):
    for w in range(1, n+1):
        for start_x in range(0, n-w+1):
            for start_y in range(0, n-w+1):
                m = get_max(start_x, start_y, w, cs)
                update(m-(w*w), start_x, start_y, w, vs)
    for row in vs:
        print(' '.join(map(str, row)))                


def main():
    cs = []
    vs = []
    n = read_single_int()
    for _ in range(n):
        cs.append(read_list_int())
        vs.append([0 for _ in range(n)])
    solution(n, cs, vs)


if __name__ == '__main__':
    main()