# Title: Christmas Eve Eve
# Link: https://abc115.contest.atcoder.jp/tasks/abc115_b

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(ps: list):
    max_price = max(ps)
    return sum(ps) - max_price//2


def main():
    n = read_single_int()
    ps = []
    for _ in range(n):
        ps.append(read_single_int())
    print(solution(ps))


if __name__ == '__main__':
    main()