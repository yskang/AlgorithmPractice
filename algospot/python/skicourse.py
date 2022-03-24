# Title: 스키코스
# Link: https://www.acmicpc.net/problem/skicourse

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

INF = 10**10


def get_excite(n: int, s: int, slopes: defaultdict, cache: list):
    if cache[n][s] != -1:
        return cache[n][s]

    if s < 1:
        cache[n][s] = 0
        return 0

    max_excite = 0

    for child, ex in slopes[n]:
        max_excite = max(get_excite(child, s-1, slopes, cache) + ex, max_excite)

    cache[n][s] = max_excite
    return max_excite


def solution(n: int, m: int, s: int, slopes: list):
    max_excite = 0
    cache = [[-1 for _ in range(s+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        max_excite = max(get_excite(i, s, slopes, cache), max_excite)
    return max_excite
                    

def main():
    t = read_single_int()
    for _ in range(t):
        n, m, s = read_list_int()
        slopes = [[] for _ in range(n+1)]

        for _ in range(m):
            a, b, c = read_list_int()
            slopes[a].append((b, c))

        print(solution(n, m, s, slopes))


if __name__ == '__main__':
    main()