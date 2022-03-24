# Title: 복불복으로 지구멸망
# Link: https://www.acmicpc.net/problem/17358

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


MOD = 1000000007


def solution(n: int):
    dp = 1
    
    for i in range(2, n+1, 2):
        dp = ((i-1) * (dp % MOD))%MOD

    return dp


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()