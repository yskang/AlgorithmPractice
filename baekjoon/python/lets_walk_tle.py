# Title: 전구 길만 걷자
# Link: https://www.acmicpc.net/problem/17359

import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_single_str = lambda: sys.stdin.readline().strip()


def solution(n: int, bulbs: list):
    counts = []
    for l in permutations(bulbs, n):
        t = ''.join(l)
        counts.append(t.count('01') + t.count('10'))
    return min(counts)


def main():
    n = read_single_int()
    bulbs = []
    for _ in range(n):
        bulbs.append(read_single_str())
    print(solution(n, bulbs))


if __name__ == '__main__':
    main()