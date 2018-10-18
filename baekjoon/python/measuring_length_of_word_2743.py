# Title: 단어 길이 재기
# Link: https://www.acmicpc.net/problem/2743

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def solution(s):
    return len(s)


def main():
    s = read_single_str()
    print(solution(s))


if __name__ == '__main__':
    main()