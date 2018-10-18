# Title: 문자열 분석
# Link: https://www.acmicpc.net/problem/10820

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().replace('\n', '')


def solution(s: str):
    low, upper, number, space = 0, 0, 0, 0

    for c in s:
        if c.isdigit():
            number += 1
        elif c.islower():
            low += 1
        elif c.isupper():
            upper += 1
        elif c.isspace():
            space += 1

    return '{} {} {} {}'.format(low, upper, number, space)


def main():
    while True:
        s = read_single_str()
        if s == '':
            break
        print(solution(s))


if __name__ == '__main__':
    main()