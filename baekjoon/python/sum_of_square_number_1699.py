# Title: 제곱수의 합
# Link: https://www.acmicpc.net/problem/1699

import sys
import bisect

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    d = [i for i in range(n+2)]
    ss = [i*i for i in range(n+2)]

    for i in range(1, n+1):
        p = bisect.bisect_right(ss, i)
        d[i] = min([d[i-ss[k]]+1 for k in range(1, p)])

    return d[n]


def main():
    N = read_single_int()
    print(solution(N))


if __name__ == '__main__':
    main()