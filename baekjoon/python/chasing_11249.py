# Title: Chasing
# Link: https://www.acmicpc.net/problem/11249

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(track_size: int, hare: int, tortoise: int):
    if hare - tortoise == 1:
        return 0
    if hare > tortoise:
        return track_size - hare + tortoise
    else:
        return tortoise - hare


def main():
    k = read_single_int()
    for _ in range(k):
        n, r, t = read_list_int()
        print(solution(n, r, t))


if __name__ == '__main__':
    main()