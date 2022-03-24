# Title: 상근날드
# Link: https://www.acmicpc.net/problem/5543

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(bugers: list, drinks: list):
    return min(bugers) + min(drinks) - 50


def main():
    bugers = []
    for _ in range(3):
        bugers.append(read_single_int())
    drinks = []
    for _ in range(2):
        drinks.append(read_single_int())

    print(solution(bugers, drinks))


if __name__ == '__main__':
    main()