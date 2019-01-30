# Title: 제로
# Link: https://www.acmicpc.net/problem/10773

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def main():
    k = read_single_int()
    ns = []
    for _ in range(k):
        n = read_single_int()
        if n == 0:
            ns.pop()
        else:
            ns.append(n)
    print(sum(ns))


if __name__ == '__main__':
    main()