# Title: SIGMA
# Link: https://www.acmicpc.net/problem/13172

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list, ss: list):
    ans = 0
    for i in range(n):
        ans += (ss[i]*pow(ns[i], 1000000005, 1000000007))%1000000007
        ans %= 1000000007
    return ans


def main():
    n = read_single_int()
    ns = []
    ss = []
    for _ in range(n):
        a, b = read_list_int()
        ns.append(a)
        ss.append(b)
    print(solution(n, ns, ss))


if __name__ == '__main__':
    main()