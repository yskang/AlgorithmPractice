# Title: 가장 긴 증가하는 부분 수열 4
# Link: https://www.acmicpc.net/problem/14002

import sys
from bisect import bisect_left


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list):
    ms = [ns[0]]
    p = [1]
    for x in ns[1:]:
        i = bisect_left(ms, x)
        if i == len(ms):
            ms.append(x)
            p.append(i+1)
        else:
            ms[i] = x
            p.append(i+1)
    
    ans = []
    print(len(ms))
    target = len(ms)
    for i in range(len(p)-1, -1, -1):
        if p[i] == target:
            ans.append(ns[i])
            target -= 1
            if target == 0:
                break
    print(*list(reversed(ans)))


def main():
    n = read_single_int()
    ns = read_list_int()
    solution(n, ns)


if __name__ == '__main__':
    main()