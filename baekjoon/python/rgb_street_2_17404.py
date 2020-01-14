# Title: RGB거리 2
# Link: https://www.acmicpc.net/problem/17404

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

RED = 0
GREEN = 1
BLUE = 2


def get_min_cost(start_color: int, costs: list, index: int, first_color: int, cache: list):
    if index <= len(costs)-2:
        if cache[(start_color, index, first_color)] != -1:
            return cache[(start_color, index, first_color)]
        cost = costs[index][start_color] + min(get_min_cost((start_color+1)%3, costs, index+1, first_color, cache), get_min_cost((start_color+2)%3, costs, index+1, first_color, cache))
        cache[(start_color, index, first_color)] = cost
        return cost
    elif index == len(costs)-1:
        if start_color == first_color:
            return 10*10**10
        else:
            return costs[index][start_color]


def solution(n: int, costs: list):
    cache = defaultdict(lambda: -1)
    return min(get_min_cost(RED, costs, 0, RED, cache), 
                get_min_cost(GREEN, costs, 0, GREEN, cache),
                get_min_cost(BLUE, costs, 0, BLUE, cache))


def main():
    n = read_single_int()
    costs = []
    for _ in range(n):
        costs.append(read_list_int())
    print(solution(n, costs))


if __name__ == '__main__':
    main()