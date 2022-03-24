# Title: 조합 0의 개수
# Link: https://www.acmicpc.net/problem/2004

import sys
import collections

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))



def solution(n: int, m: int):
    twos, fives = 0, 0

    i = 2
    while i <= n:
        twos += (n // i)
        i *= 2
    i = 2
    while i <= m:
        twos -= (m // i)
        i *= 2
    i = 2
    while i <= (n-m):
        twos -= ((n-m) // i)
        i *= 2
    i = 5
    while i <= n:
        fives += (n // i)
        i *= 5
    i = 5
    while i <= m:
        fives -= (m // i)
        i *= 5
    i = 5
    while i <= (n-m):
        fives -= ((n-m) // i)
        i *= 5

    return min(twos, fives)


def main():
    n, m = read_list_int()
    print(solution(n, m))


if __name__ == '__main__':
    main()
