# Title: 2xn 타일링
# Link: https://www.acmicpc.net/problem/11726

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

DIV = 10007

def solution(n: int):
    ns = [i for i in range(n+1)]
    for i, n in enumerate(ns[3:], 3):
        ns[i] = ns[i-1]%DIV + ns[n-2]%DIV
    return ns[-1]%DIV


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()