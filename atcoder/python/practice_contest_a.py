# Title: Welcome to AtCoder
# Link: https://practice.contest.atcoder.jp/tasks/practice_1

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_str = lambda: sys.stdin.readline().strip()


def solution(a: int, b: int, c: int, s: str):
    return '{} {}'.format(a+b+c, s)


def main():
    a = read_single_int()
    b, c = read_list_int()
    s = read_single_str()
    print(solution(a, b, c, s))


if __name__ == '__main__':
    main()