# Title: 버블 소트
# Link: https://www.acmicpc.net/problem/1517

import sys


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def sort(aa: list, start: int, end: int):
    if start >= end:
        return 0

    mid = (start + end) // 2
    count = sort(aa, start, mid) + sort(aa, mid+1, end)

    i, j = start, mid+1
    temp = []
    while i <= mid and j <= end:
        if aa[i] <= aa[j]:
            temp.append(aa[i])
            i += 1
        else:
            temp.append(aa[j])
            j += 1
            count += (mid - i + 1)

    while i <= mid:
        temp.append(aa[i])
        i += 1
    while j <= end:
        temp.append(aa[j])
        j += 1

    for i in range(start, end+1):
        aa[i] = temp[i-start]

    return count


def solution(n: int, aa: list):
    return sort(aa, 0, n-1)


def main():
    n = read_single_int()
    aa = read_list_int()
    print(solution(n, aa))


if __name__ == '__main__':
    main()