# Title: 가장 긴 감소하는 부분 수열
# Link: https://www.acmicpc.net/problem/11722

import sys
import bisect

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(ns: list, size: int):
    lis = []
    for n in reversed(ns):
        p = bisect.bisect_left(lis, n)
        if p == len(lis):
            lis.append(n)
        else:
            if n < lis[p]:
                lis[p] = n
    return len(lis)


def main():
    N = read_single_int()
    ns = read_list_int()
    print(solution(ns, N))


if __name__ == '__main__':
    main()