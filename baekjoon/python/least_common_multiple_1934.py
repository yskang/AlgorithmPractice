# Title: 최소공배수
# Link: https://www.acmicpc.net/problem/1934

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_gcd(nums):
    while nums[1] != 0:
        r = nums[0] % nums[1]
        nums[0] = nums[1]
        nums[1] = r
    return nums[0]


def get_lcm(nums):
    return nums[0] * nums[1] // get_gcd(nums)


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        print(get_lcm(read_list_int()))