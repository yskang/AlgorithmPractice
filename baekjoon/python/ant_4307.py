# Title: 개미
# Link: https://www.acmicpc.net/problem/4307

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(l: int, n: int, ants: list):
    fast, slow = 0, 0

    for ant in ants:
        fast = max(fast, min(l-ant, ant))
        slow = max(slow, max(ant, l-ant))

    return '{} {}'.format(fast, slow)


def main():
    t = read_single_int()
    for _ in range(t):
        l, n = read_list_int()
        ants = []
        for _ in range(n):
            ants.append(read_single_int())

        print(solution(l, n, ants))


if __name__ == '__main__':
    main()