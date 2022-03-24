# Title: 윷놀이
# Link: https://www.acmicpc.net/problem/2490

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_score(sticks):
    score = ['D', 'C', 'B', 'A', 'E']
    return score[sum(sticks)]


if __name__ == '__main__':
    for _ in range(3):
        print(get_score(read_list_int()))