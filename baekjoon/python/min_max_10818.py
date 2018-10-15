# Title: 최소, 최대
# Link: https://www.acmicpc.net/problem/10818

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def solution(ns: list):
    return min(ns), max(ns)


def main():
    N = read_single_int()
    ns = read_list_int()
    print('{} {}'.format(*solution(ns)))


if __name__ == '__main__':
    main()