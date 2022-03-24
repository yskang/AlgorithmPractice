# Title: 동전 0
# Link: https://www.acmicpc.net/problem/11047

import sys
from collections import defaultdict as ddict


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())

INF = 99999999999


def solution(n: int, k: int, ns: list):
    count = 0
    while True:
        coin = ns.pop()
        if k >= coin:
            d, r = divmod(k, coin)
            if r == 0:
                return count + d
            else:
                count += d
                k = r
    return -1
    

def main():
    n, k = read_list_int()
    ns = []
    for _ in range(n):
        ns.append(read_single_int())
    print(solution(n, k, ns))


if __name__ == '__main__':
    main()