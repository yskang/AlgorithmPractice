# Title: 카드2
# Link: https://www.acmicpc.net/problem/2164

import sys
from collections import deque as dq

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    d = dq([i for i in range(1, n+1)])
    while len(d) > 1:
        d.popleft()
        d.append(d.popleft())
    return d[0]


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()