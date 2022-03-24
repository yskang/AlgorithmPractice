# Title: 막대기
# Link: https://www.acmicpc.net/problem/1094

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def make_stick(x):
    sticks = [64]
    while sum(sticks) > x:
        shortest = sticks.pop()
        sticks.append(shortest//2)
        if sum(sticks) < x:
            sticks.append(shortest//2)

    return len(sticks)


def count_ones(x):
    return bin(x).count('1')


if __name__ == '__main__':
    x = read_single_int()
    # print(make_stick(x))
    print(count_ones(x))