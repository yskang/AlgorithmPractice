# Title: 되팔렘
# Link: https://www.acmicpc.net/problem/3812

import sys


sys.setrecursionlimit(10 ** 6)


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def solution(c: int, n: int, p: int, ns: list, ps: list) -> list:
    value_costs = []
    for pp in ps:
        pp.reverse()
        pp.pop()
        value = 0
        cost = 0
        while pp:
            number = pp.pop()
            count = pp.pop()
            value += (ns[number][1] - ns[number][0]) * count
            cost += ns[number][0] * count
        if value > 0 and cost <= c:
            value_costs.append((value, cost))

    value_costs.sort(key=lambda x: x[0]/x[1], reverse=True)

    max_profit = [0]
    knapsack(-1, 0, 0, c, max_profit, value_costs)

    return max_profit[0]


def knapsack(i: int, profit: int, weight: int, total_weight: int, max_profit: list, value_costs: list):
    if weight <= total_weight and profit > max_profit[0]:
        max_profit[0] = profit
    if promising(i, profit, weight, total_weight, value_costs, max_profit):
        knapsack(i+1, profit + value_costs[i+1][0], weight + value_costs[i+1][1], total_weight, max_profit, value_costs)
        knapsack(i+1, profit, weight, total_weight, max_profit, value_costs)


def promising(i: int, profit: int, weight: int, total_weight: int, value_costs: list, max_profit: list):
    if weight >= total_weight:
        return False
    j = i+1
    bound = profit
    totweight = weight
    while j < len(value_costs) and totweight + value_costs[j][1] <= total_weight:
        totweight += value_costs[j][1]
        bound += value_costs[j][0]
        j += 1
    k = j
    if k < len(value_costs):
        bound += (total_weight - totweight) * value_costs[k][0] / value_costs[k][1]
    return bound > max_profit[0]


def main():
    c = read_single_int()
    n, p = read_list_int()
    ns = [0 for _ in range(n+1)]
    for i in range(n):
        a, b = read_list_int()
        ns[i+1] = (a, b)
    ps = []
    for i in range(p):
        ps.append(read_list_int())
    print(solution(c, n, p, ns, ps))


if __name__ == '__main__':
    main()