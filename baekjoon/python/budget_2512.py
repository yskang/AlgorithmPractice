# Title: 예산
# Link: https://www.acmicpc.net/problem/2512

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list, m: int):
    max_limit = 0
    start = 0
    end = 100000

    if sum(ns) <= m:
        return max(ns)

    while True:
        if end - start < 2:
            return max_limit
        limit = start + (end-start)//2
        total = 0
        for r in ns:
            total += r if r <= limit else limit
        if total <= m:
            start = limit
            max_limit = limit
        elif total > m:
            end = limit
    

def main():
    n = read_single_int()
    ns = read_list_int()
    m = read_single_int()
    print(solution(n, ns, m))


if __name__ == '__main__':
    main()