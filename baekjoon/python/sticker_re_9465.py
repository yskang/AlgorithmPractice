# Title: 스티커
# Link: https://www.acmicpc.net/problem/9465

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_score(n: int, up: int, sticker: list, cache: list):
    if cache[up][n] != -1:
        return cache[up][n]

    if n == len(sticker[0])-1:
        d = sticker[0][n] if up else sticker[1][n]
        cache[up][n] = d
        return d
    elif n == len(sticker[0])-2:
        d = (sticker[0][n] + sticker[1][n+1]) if up else (sticker[1][n] + sticker[0][n+1])
        cache[up][n] = d
        return d
    d = (sticker[0][n] if up else sticker[1][n]) + max(get_score(n+1, not up, sticker, cache), get_score(n+2, not up, sticker, cache))
    cache[up][n] = d
    return d


def solution(n: int, stickers: list):
    cache = [[-1 for _ in range(n)] for _ in range(2)]
    return max(get_score(0, 0, stickers, cache), get_score(0, 1, stickers, cache))


def main():
    t = read_single_int()
    for _ in range(t):
        n = read_single_int()
        stickers = []
        stickers.append(read_list_int())
        stickers.append(read_list_int())
        print(solution(n, stickers))


if __name__ == '__main__':
    main()