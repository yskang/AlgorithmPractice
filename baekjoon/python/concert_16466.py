# Title: 콘서트
# Link: https://www.acmicpc.net/problem/16466

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list):
    tickets = [False for _ in range(1000001)]
    for i in ns:
        tickets[i] = True
    for i in range(1, 1000001):
        if tickets[i] == False:
            return i
    return 1000000


def main():
    n = read_single_int()
    ns = read_list_int()
    print(solution(n, ns))


if __name__ == '__main__':
    main()