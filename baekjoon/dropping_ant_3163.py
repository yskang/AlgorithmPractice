# Title: 떨어지는 개미
# Link: https://www.acmicpc.net/problem/3163

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def find_kth_ant(L, K, ants):
    drops_left, drops_right = [], []
    for ant in ants:
        if ant[1] < 0:
            drops_left.append((ant[0], ant[1]))
        else:
            drops_right.append((L-ant[0], ant[1]))
    drops = list(zip(drops_left + drops_right, ants))
    drops = sorted(sorted(drops, key=lambda drop: drop[1][1]), key=lambda drop: drop[0][0])
    return drops[K-1][1][1]


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        N, L, K = read_list_int()
        ants = []
        for _ in range(N):
            p, a = read_list_int()
            ants.append((p, a))
        print(find_kth_ant(L, K, ants))