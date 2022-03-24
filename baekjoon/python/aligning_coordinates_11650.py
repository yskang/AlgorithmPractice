# Title: 좌표 정렬하기
# Link: https://www.acmicpc.net/problem/11650

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(coords: list):
    return sorted(coords)


def main():
    N = read_single_int()
    coord = []
    for _ in range(N):
        x, y = read_list_int()
        coord.append((x, y))
    for xy in solution(coord):
        print('{} {}'.format(xy[0], xy[1]))


if __name__ == '__main__':
    main()