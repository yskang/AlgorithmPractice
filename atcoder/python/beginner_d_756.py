# Title: count all Shichi-Go numbers in N!
# Link: https://abc114.contest.atcoder.jp/tasks/abc114_d

import sys
import collections

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def add_power(n: int, ps: list):
    i = 2
    while n != 1:
        if n % i == 0:
            n = n // i
            ps[i] += 1
        else:
            i += 1


def solution(n: int):
    ps = [0 for _ in range(n+1)]

    for i in range(2, n+1):
        add_power(i, ps)

    powers = collections.defaultdict(lambda: 0)

    for p in range(2, n+1):
        powers[p] = len(list(filter(lambda x: x >= p, ps)))

    return powers[74] + powers[24] * (powers[2]-1) + powers[14] * (powers[4]-1) + powers[4] * (powers[4]-1) * (powers[2]-2)//2


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()