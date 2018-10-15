# Title: K번째 수
# Link: https://www.acmicpc.net/problem/11004

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def selection_sort(nums, k):
    sorted_index = 0
    while True:
        minimum = 9999999999
        min_index = 0
        for i, n in enumerate(nums[sorted_index:], sorted_index):
            if n < minimum:
                minimum = n
                min_index = i
        k -= 1
        if k == 0:
            return minimum
        nums[sorted_index], nums[min_index] = nums[min_index], nums[sorted_index]
        sorted_index += 1


def partition(nums, left, right, pivot_index):
    pivot_value = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left
    for i in range(left, right):
        if nums[i] < pivot_value:
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1
    nums[right], nums[store_index] = nums[store_index], nums[right]
    return store_index


def quick_select(nums, left, right, k):
    while True:
        if left == right:
            return nums[left]
        pivot_index = right
        pivot_index = partition(nums, left, right, pivot_index)
        if k-1 == pivot_index:
            return nums[k-1]
        elif k-1 < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1


def get_kth_number(nums, k):
    # TLE
    # selection_sort(nums, k)
    return quick_select(nums, 0, len(nums)-1, k)


if __name__ == '__main__':
    N, K = read_list_int()
    A = read_list_int()
    print(get_kth_number(A, K))
