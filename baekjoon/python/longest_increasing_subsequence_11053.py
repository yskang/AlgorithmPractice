# Title: 가장 긴 증가하는 부분 수열
# Link: https://www.acmicpc.net/problem/11053

import sys
import bisect


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_LIS_length_N2(nums: list, length: int):
    lis_list = [1 for _ in range(length)]
    for i in range(length):
        for j in range(i):
            if nums[j] < nums[i]:
                lis_list[i] = max(lis_list[j] + 1, lis_list[i])

    return max(lis_list)


def get_LIS_length_NlogN(nums: list, length: int):
    lis_list = [0]

    for num in nums:
        i = bisect.bisect_left(lis_list, num)
        if len(lis_list) == i:
            lis_list.append(num)
        else:
            lis_list[i] = num

    return len(lis_list)-1


def main():
    l = read_single_int()
    a = read_list_int()
    # print(get_LIS_length_N2(a, l))
    print(get_LIS_length_NlogN(a, l))


if __name__ == '__main__':
    main()