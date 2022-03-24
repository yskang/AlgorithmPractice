# Title: 과일 서리
# Link: https://www.acmicpc.net/problem/17213

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def dp(kinds: int, count: int, cache: list):
    if cache[kinds][count] != -1:
        return cache[kinds][count]
    if kinds == 1:
        cache[kinds][count] = 1
        return 1
    if kinds == count:
        cache[kinds][count] = 1
        return 1
    ans = 0
    for i in range(kinds-1, count):
        ans += dp(kinds-1, i, cache)
    cache[kinds][count] = ans
    return ans


def solution(n: int, m: int):
    cache = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    return dp(n, m, cache)


def main():
    n = read_single_int()
    m = read_single_int()
    print(solution(n, m))


if __name__ == '__main__':
    main()