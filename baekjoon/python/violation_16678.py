# Title: 모독
# Link: https://www.acmicpc.net/problem/16678

import sys

read_single_int = lambda: int(sys.stdin.readline().strip())

sys.setrecursionlimit(10 ** 6)


def solution(n: int, nums: list):
    nums = sorted(nums)
    hackers = 0
    last = 0
    for k in nums:
        if not (k == last or k == last+1):
            hackers += k - (last+1)
            k = last + 1
            last = k
        else:
            last = k
    return hackers


def main():
    n = read_single_int()
    nums = []
    for _ in range(n):
        nums.append(read_single_int())
    print(solution(n, nums))


if __name__ == '__main__':
    main()