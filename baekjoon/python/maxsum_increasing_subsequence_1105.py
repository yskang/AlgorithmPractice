# Title: 가장 큰 증가 부분 수열
# Link: https://www.acmicpc.net/problem/1105

import sys
import bisect

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def solution(ns: list, length: int):
    inc_seq = ns[:]
    max_sum = 0
    for i in range(length):
        for j in range(i):
            if ns[j] < ns[i]:
                inc_seq[i] = max(inc_seq[j]+ns[i], inc_seq[i])
        max_sum = max(inc_seq[i], max_sum)
    return max_sum


def main():
    length = read_single_int()
    A = read_list_int()
    print(solution(A, length))


if __name__ == '__main__':
    main()