# Title: 나의 행렬곱셈 답사기
# Link: https://www.acmicpc.net/problem/12796

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_matrix(K):
    print(3)
    print('1 10 {} 1'.format(K+10))


if __name__ == '__main__':
    K = read_single_int()
    get_matrix(K)
