# Title: 검문
# Link: https://www.acmicpc.net/problem/2981
import math
import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a


def get_divisors(nums):
    # get diff array diffs
    diffs = []
    prev = nums[0]
    for num in nums[1:]:
        diffs.append(num-prev)
        prev = num
    # get gcd of all diffs
    if len(diffs) >= 2:
        diff_gcd = gcd(diffs[0], diffs[1])
        for diff in diffs[2:]:
            diff_gcd = gcd(diff_gcd, diff)
    else:
        diff_gcd = diffs[0]
    # get all divisor of diff_gcd
    all_divisors = []
    for i in range(2, int(math.sqrt(diff_gcd))+1):
        if diff_gcd % i == 0:
            all_divisors.append(i)
    for n in range(len(all_divisors)-1, -1, -1):
        temp = diff_gcd//all_divisors[n]
        if all_divisors[-1] != temp:
            all_divisors.append(temp)

    all_divisors.append(diff_gcd)
    return ' '.join(map(str, all_divisors))


if __name__ == '__main__':
    N = read_single_int()
    nums = []
    for _ in range(N):
        nums.append(read_single_int())
    print(get_divisors(sorted(nums)))
