# Title: 연속합
# Link: https://www.acmicpc.net/problem/1912

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_max_sum(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = dp[0]
    for i, num in enumerate(nums[1:], 1):
        dp[i] = max(nums[i], num + dp[i-1])
        max_sum = max(max_sum, dp[i])
    return max_sum


if __name__ == '__main__':
    n = read_single_int()
    nums = read_list_int()
    print(get_max_sum(nums))