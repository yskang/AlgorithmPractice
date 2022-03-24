# Title: 1로 만들기
# Link: https://www.acmicpc.net/problem/1463

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())

INF = 9999999999


def solution(n: int):
    cache = [-1 for _ in range(n+1)]
    cache[1] = 0

    for i in range(2, n+1):
        d = cache[i-1] + 1
        if i % 2 == 0:
            d = min(cache[i//2]+1, d)
        if i % 3 == 0:
            d = min(cache[i//3]+1, d)
        cache[i] = d
    
    return cache[n]


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()