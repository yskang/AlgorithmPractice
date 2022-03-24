# Title: 쇠막대기
# Link: https://www.acmicpc.net/problem/10799

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def solution(iron: str):
    iron = iron.replace('()', '*')
    parts = 0
    num_iron = 0
    for c in iron:
        if c == '(':
            num_iron += 1
        elif c == ')':
            num_iron -= 1
            parts += 1
        elif c == '*':
            parts += num_iron

    return parts


def main():
    iron = read_single_str()
    print(solution(iron))


if __name__ == '__main__':
    main()
