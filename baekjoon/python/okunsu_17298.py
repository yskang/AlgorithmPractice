# Title: 오큰수
# Link: https://www.acmicpc.net/problem/17298

import sys
from bisect import bisect_left
from collections import deque


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


INF = 9999999999


def solution(n: int, ns: list):
    ans = []
    stack = [INF]
    for i in range(n-1, -1, -1):
        while stack[-1] <= ns[i]:
            stack.pop()
        if stack[-1] >= INF:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(ns[i])
    return reversed(ans)


def main():
    n = read_single_int()
    ns = read_list_int()
    print(*solution(n, ns))


if __name__ == '__main__':
    main()