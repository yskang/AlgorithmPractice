# Title: 로프
# Link: https://www.acmicpc.net/problem/2217

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, ropes: list):
    ropes = sorted(ropes)
    max_weight = 0
    for i, rope in enumerate(ropes):
        max_weight = max(max_weight, rope *(n-i))
    return max_weight


def main():
    n = read_single_int()
    ropes = []
    for _ in range(n):
        ropes.append(read_single_int())
    print(solution(n, ropes))


if __name__ == '__main__':
    main()