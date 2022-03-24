# Title: N 포커
# Link: https://www.acmicpc.net/problem/16565

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def combination(n: int, k: int):
    if k == n:
        return 1
    elif k == 1:
        return n
    else:
        return combination(n-1, k-1) + combination(n-1, k)


def solution(n: int):
    combination(52, n)



def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()