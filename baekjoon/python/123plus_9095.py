# Title: 1,2,3 더하기
# Link: https://www.acmicpc.net/problem/9095

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(n: int):
    d = [0 for _ in range(12)]
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    return d[n]


def main():
    T = read_single_int()
    for _ in range(T):
        n = read_single_int()
        print(solution(n))


if __name__ == '__main__':
    main()