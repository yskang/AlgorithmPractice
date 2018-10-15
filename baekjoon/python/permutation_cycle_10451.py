# Title: 순열 사이클
# Link: https://www.acmicpc.net/problem/10451

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_permutation_count(l, N):
    visits = [False for _ in range(N+1)]
    count = 0
    for i in range(1, N+1):
        if visits[i]:
            continue
        visits[i] = True
        n = l[i]
        while not visits[n]:
            visits[n] = True
            n = l[n]
        count += 1
    return count


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        N = read_single_int()
        l = read_list_int()
        print(get_permutation_count([0]+l, N))