# Title: 스티커
# Link: https://www.acmicpc.net/problem/9465

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(scores: list, length: int):
    skip = [0 for _ in range(length)]
    up = [0 for _ in range(length)]
    down = [0 for _ in range(length)]

    skip[0] = 0
    up[0] = scores[0][0]
    down[0] = scores[1][0]

    for i in range(1, length):
        up[i] = scores[0][i] + max(skip[i-1], down[i-1])
        down[i] = scores[1][i] + max(skip[i-1], up[i-1])
        skip[i] = max(skip[i-1], up[i-1], down[i-1])

    return max(up[-1], down[-1], skip[-1])


def main():
    T = read_single_int()
    for _ in range(T):
        scores = []
        n = read_single_int()
        scores.append(read_list_int())
        scores.append(read_list_int())
        print(solution(scores, n))


if __name__ == '__main__':
    main()