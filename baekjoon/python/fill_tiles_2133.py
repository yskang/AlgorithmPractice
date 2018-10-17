# Title: 타일 채우기
# Link: https://www.acmicpc.net/problem/2133

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(n: int):
    d = [0 for _ in range(n+2)]
    d[0] = 1
    d[2] = 3
    for i in range(4, n+1, 2):
        d[i] = d[i-2]*3 + sum([d[i-j]*2 for j in range(4, i+1, 2)])
    return d[n]


def main():
    N = read_single_int()
    print(solution(N))


if __name__ == '__main__':
    main()