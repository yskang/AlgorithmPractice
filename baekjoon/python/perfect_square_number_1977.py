# Title: 완전제곱수
# Link: https://www.acmicpc.net/problem/1977
import math
import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def perfect_square_number(M, N):
    nums = []
    for n in range(M, N+1):
        if math.sqrt(n).is_integer():
            nums.append(n)
    if nums:
        sum_of_them = sum(nums)
        minimum_number = min(nums)
        return '\n'.join(map(str, [sum_of_them, minimum_number]))
    else:
        return '-1'


if __name__ == '__main__':
    M = read_single_int()
    N = read_single_int()
    print(perfect_square_number(M, N))