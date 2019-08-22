# Title: 연산자 끼워넣기
# Link: https://www.acmicpc.net/problem/14888

import sys
from itertools import permutations
from collections import defaultdict
from copy import deepcopy

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution_bf(n: int, ns: list, ops: list):
    minimum = 10000000000
    maximum = -minimum

    cach = defaultdict(lambda: False)
    operators = [0]*ops[0] + [1]*ops[1] + [2]*ops[2] + [3]*ops[3]
    for operation in permutations(operators):
        op_str = ''.join(map(str, operation))
        if cach[op_str]:
            continue
        cach[op_str] = True

        res = ns[0]
        for i, x in enumerate(ns[1:]):
            if operation[i] == 0:
                res += x
            elif operation[i] == 1:
                res -= x
            elif operation[i] == 2:
                res *= x
            else:
                minus = False
                if res < 0:
                    minus = True
                res = abs(res)//x
                if minus:
                    res = -res

        minimum = min(minimum, res)
        maximum = max(maximum, res)

    return '{}\n{}'.format(maximum, minimum)


def dfs_long_time(ns: list, operations: list, res: int, minimum: list, maximum: list, visited: list, idx: int, op_idx: int, call: list):
    call[0] = call[0] + 1
    ans = 0
    if idx == len(ns):
        minimum[0] = min(minimum[0], res)
        maximum[0] = max(maximum[0], res)
        visited[op_idx] = False
        return

    for i, op in enumerate(operations):
        if visited[i]:
            continue
        visited[i] = True

        if op == 0:
            ans = res + ns[idx]
        elif op == 1:
            ans = res - ns[idx]
        elif op == 2:
            ans = res * ns[idx]
        else:
            sign_a, sign_b = 1, 1
            if res < 0:
                sign_a = -1
            if ns[idx] < 0:
                sign_b = -1
            ans = (abs(res)//abs(ns[idx])) * (sign_a * sign_b)
        dfs_long_time(ns, operations, ans, minimum, maximum, visited, idx+1, i, call)
    visited[op_idx] = False


def solution_dfs(n: int, ns: list, ops: list):
    call = [0]
    operations = [0]*ops[0] + [1]*ops[1] + [2]*ops[2] + [3]*ops[3]
    minimum, maximum = [10**10], [-10**10]
    visited = [False for _ in range(n-1)]
    dfs_long_time(ns, operations, ns[0], minimum, maximum, visited, 1, 0, call)
    return '{}\n{}\n{}'.format(maximum[0], minimum[0], call[0])


def dfs(ns: list, idx: int, res: int, plus: int, minus: int, multiples: int, divides: int, minimum: list, maximum: list, call: list):
    call[0] = call[0] + 1
    if idx == len(ns):
        minimum[0] = min(minimum[0], res)
        maximum[0] = max(maximum[0], res)
        return

    if plus:
        dfs(ns, idx+1, res+ns[idx], plus-1, minus, multiples, divides, minimum, maximum, call)
    if minus:
        dfs(ns, idx+1, res-ns[idx], plus, minus-1, multiples, divides, minimum, maximum, call)
    if multiples:
        dfs(ns, idx+1, res*ns[idx], plus, minus, multiples-1, divides, minimum, maximum, call)
    if divides:
        sign_a = 1 if res > 0 else -1
        sign_b = 1 if ns[idx] > 0 else -1
        dfs(ns, idx+1, sign_a*sign_b*(abs(res)//abs(ns[idx])), plus, minus, multiples, divides-1, minimum, maximum, call)


def solution(n: int, ns: list, ops: list):
    minimum, maximum = [10**10], [-10**10]
    call = [0]
    dfs(ns, 1, ns[0], ops[0], ops[1], ops[2], ops[3], minimum, maximum, call)
    return '{}\n{}'.format(maximum[0], minimum[0])


def main():
    n = read_single_int()
    ns = read_list_int()
    ops = read_list_int()
    print(solution(n, ns, ops))
    # print(solution_dfs(n, ns, ops))


if __name__ == '__main__':
    main()