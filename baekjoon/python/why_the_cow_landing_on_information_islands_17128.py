# Title: 소가 정보섬에 올라온 이유
# Link: https://www.acmicpc.net/problem/17128

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, q: int, cows: list, qs: list):
    cows = cows + cows
    parts = []
    for start in range(n):
        parts.append(cows[start]*cows[start+1]*cows[start+2]*cows[start+3])

    s = sum(parts)

    for q in qs:
        s -= 2*(parts[q-1]+parts[q-2]+parts[q-3]+parts[q-4])
        parts[q-1] *= -1
        parts[q-2] *= -1
        parts[q-3] *= -1
        parts[q-4] *= -1
        print(s)


def main():
    n, q = read_list_int()
    cows = read_list_int()
    qs = read_list_int()
    solution(n, q, cows, qs)


if __name__ == '__main__':
    main()