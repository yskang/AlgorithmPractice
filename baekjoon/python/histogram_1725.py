# Title: 히스토그램
# Link: https://www.acmicpc.net/problem/1725

import sys


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def solution(n: int, ns: list) -> int:
    stack = []
    area_max = 0
    for i, h in enumerate(ns):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            area_max = max(area_max, height * (i - idx))
            start = idx
        stack.append((start, h))
    for i, h in stack:
        area_max = max(area_max, h * (n - i))
    return area_max


def main():
    n = read_single_int()
    ns = []
    for _ in range(n):
        ns.append(read_single_int())
    print(solution(n, ns))


if __name__ == '__main__':
    main()