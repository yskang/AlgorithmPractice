# Title: 욱제가 풀어야 하는 문제
# Link: https://www.acmicpc.net/problem/18249

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

MOD = 10**9+7

def get_fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    return (get_fibonacci(n-1)%MOD + get_fibonacci(n-2)&MOD)%MOD


def solution(n: int):
    return get_fibonacci(n)


def main():
    t = read_single_int()
    for _ in range(t):
        print(solution(read_single_int()))


if __name__ == '__main__':
    main()