# Title: 벚꽃이 정보섬에 피어난 이유
# Link: https://www.acmicpc.net/problem/1712

import sys
from functools import reduce
from operator import mul, add

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_rest_sum_of_list(ns: list, depth: int):
    if depth == 2:
        temp = []
        for i in range(1, len(ns)):
            temp.append(reduce(mul, ns[:i]) + reduce(mul, ns[i:]))
        return temp

    rests = []
    for i in range(1, len(ns)):
        rests += list(map(lambda x: x+reduce(mul, ns[:i]), get_rest_sum_of_list(ns[i:], depth+1)))

    return rests


def solution(n: int, ns: list):
    return max(get_rest_sum_of_list(ns, 0))


def main():
    n = read_single_int()
    ns = read_list_int()
    print(solution(n, ns))


if __name__ == '__main__':
    main()