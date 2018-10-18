# Title: 좌표 정렬하기 2
# Link: https://www.acmicpc.net/problem/11651

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(coords: list):
    return sorted(coords, key=lambda x: (x[1], x[0]))


def main():
    N = read_single_int()
    coords = []
    for _ in range(N):
        x, y = read_list_int()
        coords.append((x, y))
    print('\n'.join(map(lambda x: '{} {}'.format(x[0], x[1]),solution(coords))))


if __name__ == '__main__':
    main()