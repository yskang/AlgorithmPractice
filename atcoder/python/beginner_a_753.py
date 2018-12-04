# Title: Shichi-Go-San
# Link: https://abc114.contest.atcoder.jp/tasks/abc114_a

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(x: int):
    if x == 3 or x == 5 or x == 7:
        return 'YES'
    return 'NO'


def main():
    x = read_single_int()
    print(solution(x))


if __name__ == '__main__':
    main()