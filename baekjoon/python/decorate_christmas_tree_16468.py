# Title: 크리스마스 트리 꾸미기
# Link: https://www.acmicpc.net/problem/16468

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


MOD = 100030001


def solution(num_ball: int, height: int):
    no_fill_table = [[1 for _ in range(301)] for _ in range(301)]
    fill_table = [[0 for _ in range(301)] for _ in range(301)]
    fill_table[1][1] = 1

    for level in range(2, height+1):
        for ball in range(2, min(pow(2, level), num_ball+1)):
            s = 0
            ss = 0
            for i in range(min(pow(2, level-1)-1, ball-1), ball-min(pow(2, level-1)-1, ball-1)-2, -1):
                s += (no_fill_table[level-1][i] * no_fill_table[level-1][ball-1-i])
                ss += (fill_table[level-1][i] * no_fill_table[level-1][ball-1-i] + (no_fill_table[level-1][i] - fill_table[level-1][i]) * fill_table[level-1][ball-1-i])


            no_fill_table[level][ball] = s % MOD
            fill_table[level][ball] = ss % MOD

    return fill_table[height][num_ball]


def main():
    n, l = read_list_int()
    print(solution(n, l))


if __name__ == '__main__':
    main()