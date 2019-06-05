# Title: 가장 큰 감소 부분 수열
# Link: https://www.acmicpc.net/problem/17216

import sys
import bisect

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def lis(length: int, ns: list):
    inc_seq_sum = ns[:]
    for i in range(length):
        for j in range(i):
            if ns[j] < ns[i]:
                inc_seq_sum[i] = max(inc_seq_sum[j]+ns[i], inc_seq_sum[i])
    return max(inc_seq_sum)


def solution(n: int, ns: list):
    ns.reverse()
    return(lis(n, ns))


def main():
    n = read_single_int()
    ns = read_list_int()
    print(solution(n, ns))


if __name__ == '__main__':
    main()