# Title: 팰린드롬?
# Link: https://www.acmicpc.net/problem/10942

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, nums: list, m: int, questions: list):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for d in range(n):
        for s in range(n-d):
            if d == 0:
                dp[s][s+d] = 1
            elif d == 1:
                if nums[s] == nums[s+d]:
                    dp[s][s+d] = 1
                else:
                    dp[s][s+d] = 0
            else:
                if dp[s+1][s+d-1] == 1 and nums[s] == nums[s+d]:
                    dp[s][s+d] = 1
                else:
                    dp[s][s+d] = 0

    for s, e in questions:
        print( dp[s-1][e-1])


def main():
    n = read_single_int()
    nums = read_list_int()
    m = read_single_int()
    questions = []
    for _ in range(m):
        questions.append(read_list_int())
    solution(n, nums, m, questions)


if __name__ == '__main__':
    main()