# Title: 계단 오르기
# Link: https://www.acmicpc.net/problem/2579

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, steps: list):
    if n == 1:
        return steps[1]

    d_1 = [0 for _ in range(n+1)]

    d_1[0] = 0
    d_1[1] = steps[1]
    d_1[2] = steps[1]+steps[2]

    for k in range(3, n+1):
        d_1[k] = max(d_1[k-3]+steps[k-1]+steps[k], d_1[k-2]+steps[k])

    return d_1[n]


def main():
    n = read_single_int()
    steps = []
    for _ in range(n):
        steps.append(read_single_int())
    print(solution(n, [0] + steps))


if __name__ == '__main__':
    main()