# Title: Interactive Sorting
# Link: https://practice.contest.atcoder.jp/tasks/practice_2

import sys
import random


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_str = lambda: sys.stdin.readline().strip()


def swap(arr: list, i: int, j: int):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr: list, start: int, end: int):
    pivot_idx = random.randint(start, end)
    pivot_val = arr[pivot_idx]

    swap(arr, pivot_idx, end)
    store = start

    for i in range(start, end):
        print('? {} {}'.format(arr[i], pivot_val))
        sys.stdout.flush()
        ans = read_single_str()
        if ans == '<':
            swap(arr, i, store)
            store += 1
    swap(arr, store, end)
    return store


def quick_sort(arr: list, start: int, end: int):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr


def solution(n: int, q: int):
    ns = [chr(i) for i in range(ord('A'), ord('A')+n)]
    ns = quick_sort(ns, 0, n-1)
    print('! {}'.format(''.join(ns)))
    sys.stdout.flush()


def main():
    n, q = read_list_int()
    solution(n, q)


if __name__ == '__main__':
    main()