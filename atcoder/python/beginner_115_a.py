# Title: Christmas Eve Eve Eve
# Link: https://abc115.contest.atcoder.jp/tasks/abc115_a

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(d: int):
    return {22:'Christmas Eve Eve Eve', 23:'Christmas Eve Eve', 24:'Christmas Eve', 25:'Christmas'}[d]


def main():
    d = read_single_int()
    print(solution(d))


if __name__ == '__main__':
    main()