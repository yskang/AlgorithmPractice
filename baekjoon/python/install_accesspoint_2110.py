# Title: 공유기 설치
# Link: https://www.acmicpc.net/problem/2110

import sys

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, ns: list, c: int):
    ns = sorted(ns)
    ans = -1
    start, end = ns[0], ns[-1]
    while True:
        if end - start < 2:
            return ans

        d = start + (end - start)//2
        installed = 1
        prev = ns[0]

        for x in ns[1:]:
            if prev + d <= x:
                prev = x
                installed += 1

        if installed < c:
            end = d
        elif installed >= c:
            start = d
            ans = d



def main():
    n, c = read_list_int()
    ns = []
    for _ in range(n):
        ns.append(read_single_int())
    print(solution(n, ns, c))


if __name__ == '__main__':
    main()