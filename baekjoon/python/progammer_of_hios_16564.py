# Title: 히오스 프로게이머
# Link: https://www.acmicpc.net/problem/16564

import sys
import heapq

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, k: int, levels: list):
    start = 0
    end = 1000000001
    ans = -1
    while True:
        if end - start < 2:
            break
        sum_up = 0
        min_level = start + (end - start)//2
        for level in levels:
            if level < min_level:
                sum_up += (min_level - level)
        
        if sum_up <= k:
            ans = min_level
            start = min_level
        elif sum_up > k:
            end = min_level

    return ans


def main():
    n, k = read_list_int()
    levels = []
    for _ in range(n):
        levels.append(read_single_int())
    print(solution(n, k, levels))


if __name__ == '__main__':
    main()