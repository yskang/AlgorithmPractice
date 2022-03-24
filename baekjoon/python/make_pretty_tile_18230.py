# Title: 2xN 예쁜 타일링
# Link: https://www.acmicpc.net/problem/18230

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, a: int, b: int, a_tiles: list, b_tiles: list):
    a_tiles = sorted(a_tiles, reverse=True)
    b_tiles = sorted(b_tiles, reverse=True)

    for i in range(1, len(a_tiles)):
        a_tiles[i] += a_tiles[i-1]
    for i in range(1, len(b_tiles)):
        b_tiles[i] += b_tiles[i-1]
    
    a_tiles = [0] + a_tiles
    b_tiles = [0] + b_tiles

    res = 0

    if n == 1:
        return a_tiles[1]

    if n == 2:
        return max(a_tiles[2], b_tiles[1])


    for i in range(min(n, len(a_tiles))):
        if (n-i)%2 == 0:
            j = (n-i)//2
            if j < len(b_tiles):
                res = max(res, a_tiles[i]+b_tiles[j])
    return res


def main():
    n, a, b = read_list_int()
    a_tiles = read_list_int()
    b_tiles = read_list_int()
    print(solution(n, a, b, a_tiles, b_tiles))


if __name__ == '__main__':
    main()