# Title: 피보나치 수 4
# Link: https://www.acmicpc.net/problem/10826

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    f = [0 for _ in range(n+1)]
    f[0], f[1], f[2] = 0, 1, 1
    for i in range(3, n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()