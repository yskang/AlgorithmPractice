# Title: 되팔렘
# Link: https://www.acmicpc.net/problem/3812

import sys
from math import gcd


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
    # print(value_costs)
    value_costs.sort(key=lambda x: x[0], reverse=True)

    unit_value = gcd(value_costs[0][1], value_costs[1][1])
    for value, cost in value_costs[2:]:
        unit_value = gcd(unit_value, cost)

    size = (c // unit_value)
    dp = [0 for _ in range(size+1)]
    dp2 = [0 for _ in range(size+1)]

    for value, cost in value_costs:
        for i in range(size+1):
            budget = i * unit_value
            if budget >= cost:
                dp2[i] = max(dp[i], dp[i-cost//unit_value] + value)
            else:
                dp2[i] = dp[i]
        dp, dp2 = dp2, dp

    return dp[-1]


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