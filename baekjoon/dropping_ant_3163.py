# Title: 떨어지는 개미
# Link: https://www.acmicpc.net/problem/3163

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def find_kth_ant(L, K, ants):
    print(ants)
    return 0


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        N, L, K = read_list_int()
        ants = []
        for _ in range(N):
            p, a = read_list_int()
            ants.append((p, a))
        print(find_kth_ant(L, K, ants))