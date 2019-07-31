# Title: 약수
# Link: https://www.acmicpc.net/problem/1037

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, divisers: list):
    divisers = sorted(divisers)
    if n == 1:
        return divisers[0] * divisers[0]
    else:
        return divisers[0] * divisers[-1]


def main():
    n = read_single_int()
    divisers = read_list_int()
    print(solution(n, divisers))


if __name__ == '__main__':
    main()