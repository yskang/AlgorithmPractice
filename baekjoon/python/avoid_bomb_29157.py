# Title: 폭탁 피하기
# Link: https://www.acmicpc.net/problem/29157

import sys
from itertools import combinations


MOD = 10**9 + 7


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def get_factorial_mod(size: int):
    factorials = [1, 1]
    for i in range(2, size+1):
        factorials.append((factorials[-1] * i) % MOD)
    return factorials


def get_inv_factorials(factorials: list):
    inv_factorials = [pow(factorials[-1], MOD-2, MOD)]
    for i in range(len(factorials)-1, 0, -1):
        inv_factorials.append((inv_factorials[-1] * i) % MOD)
    return inv_factorials[::-1]


def solution(n: int, m: int, k: int, ks: list):
    factoricals = get_factorial_mod(2000000)
    inv_factorials = get_inv_factorials(factoricals)

    # calculate total path
    total_paths = factoricals[n+m] * inv_factorials[n] * inv_factorials[m] % MOD

    # sort bomb as x position
    ks.sort(key=lambda bomb: (bomb[0], bomb[1]))

    # from 1 to K, calculate path
    for i in range(1, k+1):
        for comb in combinations(ks, i):
            bomb_path = 1
            combb = list(comb)+[(n, m)]
            prev_x, prev_y = 0, 0
            for x, y in combb:
                xd, yd = x - prev_x, y - prev_y
                if xd < 0 or yd < 0:
                    bomb_path = 0
                    break
                bomb_path *= factoricals[xd+yd] * inv_factorials[xd] * inv_factorials[yd] % MOD
                prev_x, prev_y = x, y
            if i % 2:
                total_paths -= bomb_path
            else:
                total_paths = (total_paths + bomb_path) % MOD
    return total_paths % MOD


def main():
    n, m, k = read_list_int()
    ks = []
    for _ in range(k):
        ks.append(read_list_int())
    print(solution(n, m, k, ks))


if __name__ == '__main__':
    main()