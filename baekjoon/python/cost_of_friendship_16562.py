# Title: 친구비
# Link: https://www.acmicpc.net/problem/16562

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def dfs(friends_of: list, start: int, visits: defaultdict):
    if visits[start]:
        return
    visits[start] = True
    for friend in friends_of[start]:
        dfs(friends_of, friend, visits)


def solution(n: int, m: int, k: int, values: list, friends_of: list):
    values = [0] + values
    groups = defaultdict(lambda: False)

    total_cost = 0

    for i in range(1, n+1):
        if groups[i]:
            continue
        visits = defaultdict(lambda: False)
        dfs(friends_of, i, visits)

        min_value = 999999999999999
        for key in visits.keys():
            groups[key] = True
            if values[key] < min_value:
                min_value = values[key]
        total_cost += min_value

    return total_cost if total_cost <= k else 'Oh no'


def main():
    n, m, k = read_list_int()
    values = read_list_int()
    friends_of = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = read_list_int()
        friends_of[a].append(b)
        friends_of[b].append(a)
    print(solution(n, m, k, values, friends_of))


if __name__ == '__main__':
    main()