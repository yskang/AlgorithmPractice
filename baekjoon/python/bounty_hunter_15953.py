# Title: 상금 헌터
# Link: https://www.acmicpc.net/problem/15953

import sys

sys.setrecursionlimit(10 ** 6)

first = [0] + [500] + [300] * 2 + [200] * 3 + [50] * 4 + [30] * 5 + [10] * 6 + [0] * 79
second = [0] + [512] + [256] * 2 + [128] * 4 + [64] * 8 + [32] * 16 + [0] * 69


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


if __name__ == '__main__':
    T = read_single_int()
    ans = []
    for _ in range(T):
        a, b = read_list_int()
        ans.append(str((first[a] + second[b]) * 10000))
    print('\n'.join(ans))