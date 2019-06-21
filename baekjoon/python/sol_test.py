# Title: 문제제목
# Link: https://www.acmicpc.net/problem/test

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n, ns):
    print(n)
    for x in ns:
        print(x)


def main():
    n = read_single_int()
    ns = []
    for _ in range(n):
        ns.append(read_single_int())
    solution(n, ns)


if __name__ == '__main__':
    main()