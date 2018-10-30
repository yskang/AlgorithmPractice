# Title: 경찰차
# Link: https://www.acmicpc.net/problem/2618

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

INF = 999999999999999

class Global:
    def __init__(self):
        self.dp = []
        self.events = []
        self.event_size = 0
        self.width = 0
        self.dp_a = []
        self.dp_b = []


def distance(a: tuple, b: tuple):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def min_distance(x: int, y: int, g: Global):
    if x == g.event_size or y == g.event_size:
        return 0
    if g.dp[x][y] != -1:
        return g.dp[x][y]
    first = g.dp_a[x][y] = min_distance(max(x, y)+1, y, g) + distance(g.events[max(x, y)+1], (1, 1) if x == 0 else g.events[x])
    second = g.dp_b[x][y] =  min_distance(x, max(x, y)+1, g) + distance(g.events[max(x, y)+1], (g.width, g.width) if y == 0 else g.events[y])
    g.dp[x][y] = min(first, second)
    return g.dp[x][y]


def print_route(x: int, y: int, g: Global):
    if x == g.event_size or y == g.event_size:
        return
    if g.dp_a[x][y] < g.dp_b[x][y]:
        print('1')
        print_route(max(x, y)+1, y, g)
    else:
        print('2')
        print_route(x, max(x, y)+1, g)


def solution(g: Global):
    g.dp = [[-1 for _ in range(g.event_size+1)] for _ in range(g.event_size+1)]
    g.dp_a = [[-1 for _ in range(g.event_size+1)] for _ in range(g.event_size+1)]
    g.dp_b = [[-1 for _ in range(g.event_size+1)] for _ in range(g.event_size+1)]
    g.events = [0] + g.events
    print(min_distance(0, 0, g))
    print_route(0, 0, g)


def main():
    g = Global()
    n = read_single_int()
    w = read_single_int()
    for _ in range(w):
        g.events.append(read_list_int())

    g.event_size = w
    g.width = n

    solution(g)


if __name__ == '__main__':
    main()