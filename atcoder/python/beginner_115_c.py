# Title: Christmas Eve
# Link: https://abc115.contest.atcoder.jp/tasks/abc115_c

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, k: int, hs: list):
    sorted_hs = sorted(hs)
    min_diff = 99999999999999999
    for start in range(0, n-k+1):
        diff = sorted_hs[start+k-1] - sorted_hs[start]
        if min_diff > diff:
            min_diff = diff
    return min_diff


def main():
    n, k = read_list_int()
    hs = []
    for _ in range(n):
        hs.append(read_single_int())
    print(solution(n, k, hs))


if __name__ == '__main__':
    main()