# Title: 01타일
# Link: https://www.acmicpc.net/problem/1904

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

MOD = 15746

def solution(n: int):
    res = [i for i in range(n+1)]
    for i in range(4, n+1):
        res[i] = (res[i-1] % MOD + res[i-2] % MOD)%MOD
    return res[n]


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()