# Title: 경찰차
# Link: https://www.acmicpc.net/problem/2618

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

INF = 999999999999999

dp = []
events = []
event_size = 0
width = 0
dp_a = []
dp_b = []


def distance(a: tuple, b: tuple):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def min_distance(x: int, y: int):
    global dp, dp_a, dp_b, width, events
    if x == event_size or y == event_size:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]
    first = dp_a[x][y] = min_distance(max(x, y)+1, y) + distance(events[max(x, y)+1], (1, 1) if x == 0 else events[x])
    second = dp_b[x][y] =  min_distance(x, max(x, y)+1) + distance(events[max(x, y)+1], (width, width) if y == 0 else events[y])
    dp[x][y] = min(first, second)
    return dp[x][y]


def print_route(x: int, y: int):
    global event_size, dp_a, dp_b
    if x == event_size or y == event_size:
        return
    if dp_a[x][y] < dp_b[x][y]:
        print('1')
        print_route(max(x, y)+1, y)
    else:
        print('2')
        print_route(x, max(x, y)+1)


def solution():
    global dp, dp_a, dp_b, events, event_size
    dp = [[-1 for _ in range(event_size+1)] for _ in range(event_size+1)]
    dp_a = [[-1 for _ in range(event_size+1)] for _ in range(event_size+1)]
    dp_b = [[-1 for _ in range(event_size+1)] for _ in range(event_size+1)]
    events = [0] + events
    print(min_distance(0, 0))
    print_route(0, 0)


def main():
    global events, event_size, width
    width = read_single_int()
    event_size = read_single_int()
    for _ in range(event_size):
        events.append(read_list_int())
    solution()


if __name__ == '__main__':
    main()