# Title: k번째 수
# Link: https://www.acmicpc.net/problem/1300

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, k: int):
    left = 1
    right = k
    ans = 0
    while left <= right:
        mid = (left + right)//2
        numbers_under_mid = 0
        for i in range(1, n+1):
            numbers_under_mid += min(mid//i, n)
        if numbers_under_mid >= k:
            ans = mid
            right = mid-1
        elif numbers_under_mid < k:
            left = mid+1
    return ans


def main():
    n = read_single_int()
    k = read_single_int()
    print(solution(n, k))


if __name__ == '__main__':
    main()