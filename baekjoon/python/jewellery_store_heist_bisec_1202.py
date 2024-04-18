# Title: 보석 도둑
# Link: https://www.acmicpc.net/problem/1202

import sys
from bisect import bisect_left


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def solution(jewels: list, bags: list) -> int:
    ans = 0
    bags.sort()
    jewels.sort(key=lambda x: x[0])

    for m, v in jewels:
        i = bisect_left(bags, m)
        if i < len(bags):
            ans += v
            bags[i] = bags[i-1]

    return ans


def main():
    n, k = read_list_int()
    jewels = []
    bags = []
    for _ in range(n):
        jewels.append(tuple(read_list_int()))
    for _ in range(k):
        bags.append(read_single_int())
    print(solution(jewels, bags))


if __name__ == '__main__':
    main()