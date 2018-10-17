# Title: 가장 긴 바이토닉 부분 수열
# Link: https://www.acmicpc.net/problem/11054

import sys
import bisect

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def get_inc_lengths(ns: list):
    lis = []
    incs = []
    for n in ns:
        p = bisect.bisect_left(lis, n)
        incs.append(p+1)
        if len(lis) == p:
            lis.append(n)
        else:
            lis[p] = min(lis[p], n)
    return incs

def solution(ns: list, size: int):
    inc_lengths = get_inc_lengths(ns)
    dec_lengths = get_inc_lengths(reversed(ns))
    return max(map(sum, zip(inc_lengths, reversed(dec_lengths))))-1


def main():
    N = read_single_int()
    ns = read_list_int()
    print(solution(ns, N))


if __name__ == '__main__':
    main()