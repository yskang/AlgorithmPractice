# Title: 2xn 타일링 2
# Link: https://www.acmicpc.net/problem/11727

import sys

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())

DIV = 10007


def solution(n: int):
    ns = [i for i in range(n+1)]
    if n == 1:
        return 1
    for i in range(3, n+1):
        ns[i] = ns[i-1]%DIV + (2*ns[i-2])%DIV
    return ns[n]%DIV


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()