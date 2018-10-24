# Title: 랜선 자르기
# Link: https://www.acmicpc.net/problem/1654

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(k: int, n: int, lines: list):
    lines = sorted(lines)
    left = 1
    right = lines[-1]+1
    mid = 0
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        numbers = sum(map(lambda x: x//mid, lines))
        if numbers >= n:
            left = mid+1
            if mid > ans:
                ans = mid
        elif numbers < n:
            right = mid-1

    return ans


def main():
    k, n = read_list_int()
    lines = []
    for _ in range(k):
        lines.append(read_single_int())
    print(solution(k, n, lines))


if __name__ == '__main__':
    main()