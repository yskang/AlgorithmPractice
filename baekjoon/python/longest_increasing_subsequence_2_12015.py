# Title: 가장 긴 증가하는 부분 수열 2
# Link: https://www.acmicpc.net/problem/12015

import sys
from bisect import bisect_left


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))



def solution(n: int, ns: list):
    ds = [ns[0]]

    for num in ns[1:]:
        i = bisect_left(ds, num)
        if i == len(ds):
            ds.append(num)
        else:
            ds[i] = num
    return len(ds)


def main():
    n = read_single_int()
    ns = read_list_int()
    print(solution(n, ns))


if __name__ == '__main__':
    main()