# Title: 보석 도둑
# Link: https://www.acmicpc.net/problem/1202

import sys
from heapq import heappop, heappush


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def solution(jewels: list, bags: list) -> int:
    jewels.sort(key=lambda x: x[0], reverse=True)
    bags.sort()
    ans = 0

    poped_jewels = []

    for bag in bags:
        while jewels:
            weight, value = jewels[-1]
            if weight > bag:
                break
            else:
                jewels.pop()
                heappush(poped_jewels, -value)
        if poped_jewels:
            ans += heappop(poped_jewels)
    return -ans


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