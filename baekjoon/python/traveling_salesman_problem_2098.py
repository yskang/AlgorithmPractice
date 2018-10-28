# Title: 외판원 순회
# Link: https://www.acmicpc.net/problem/2098

import sys

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split()))


def visit_city(city: int, visits: int, costs: list, total_cities: int, cache: list):
    if visits == (1<<total_cities) - 1:
        if costs[city][0] == 0:
            return 9999999999999999
        return costs[city][0]

    if cache[city][visits] != 0:
        return cache[city][visits]

    minimum = 16000001

    for last_city in range(1, total_cities):
        if visits & (1<<last_city) != 0:
            continue
        if costs[city][last_city] == 0:
            continue
        minimum = min(minimum, visit_city(last_city, visits | (1<<last_city), costs, total_cities, cache) + costs[city][last_city])

    cache[city][visits] = minimum

    return minimum



def solution(n: int, costs: list):
    cache = [[0 for _ in range(2**n+1)] for _ in range(n+1)]
    cost = visit_city(0, 1, costs, n, cache)
    return cost


def main():
    n = read_single_int()
    costs = []
    for _ in range(n):
        costs.append(read_list_int())
    print(solution(n, costs))


if __name__ == '__main__':
    main()