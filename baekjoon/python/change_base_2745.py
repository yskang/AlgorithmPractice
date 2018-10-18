# Title: 진법변환
# Link: https://www.acmicpc.net/problem/2745

import sys


sys.setrecursionlimit(10 ** 6)


read_list_word = lambda: sys.stdin.readline().strip().split(' ')


def solution(n: str, b: str):
    return int(n, int(b))


def main():
    n, b = read_list_word()
    print(solution(n, b))


if __name__ == '__main__':
    main()