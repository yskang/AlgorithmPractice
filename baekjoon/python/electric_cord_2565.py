# Title: 전깃줄
# Link: https://www.acmicpc.net/problem/2565

import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, lines: list):
    lines = sorted(lines, key=lambda l: l[0])
    bs = list(map(lambda l: l[1], lines))
    
    d = [0]

    for b in bs:
        i = bisect_left(d, b)
        if len(d) == i:
            d.append(b)
        else:
            d[i] = b

    return n - (len(d)-1)


def main():
    n = read_single_int()
    lines = []
    for _ in range(n):
        lines.append(read_list_int())
    print(solution(n, lines))


if __name__ == '__main__':
    main()