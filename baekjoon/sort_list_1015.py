# Title: 수열 정렬
# Link: https://www.acmicpc.net/problem/1015

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def sort_list(N, A):
    res = []
    sorted_a = sorted(A)
    map_a = {}

    for i in range(N-1, -1, -1):
        if sorted_a[i] in map_a:
            map_a[sorted_a[i]].append(i)
        else:
            map_a[sorted_a[i]] = [i]

    for a in A:
        res.append(str(map_a[a].pop()))
    return ' '.join(res)


if __name__ == '__main__':
    N = read_single_int()
    A = read_list_int()
    print(sort_list(N, A))