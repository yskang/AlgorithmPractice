# Title: 네 수
# Link: https://www.acmicpc.net/problem/10824

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def solution(nums: list):
    return int(nums[0] + nums[1]) + int(nums[2] + nums[3])


def main():
    nums = sys.stdin.readline().strip().split(' ')
    print(solution(nums))


if __name__ == '__main__':
    main()