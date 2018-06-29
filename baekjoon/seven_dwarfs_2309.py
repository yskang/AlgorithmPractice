# Title: 일곱 난장이
# Link: https://www.acmicpc.net/problem/2309

import sys
import itertools

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_true_dwarfs(hs):
    for chosen in itertools.permutations(hs):
        if sum(chosen[:7]) == 100:
            return '\n'.join(map(str,sorted(chosen[:7])))


if __name__ == '__main__':
    hs = []
    for _ in range(9):
        hs.append(read_single_int())
    print(get_true_dwarfs(hs))