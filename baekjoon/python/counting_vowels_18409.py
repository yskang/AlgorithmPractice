# Title: 모음 세기
# Link: https://www.acmicpc.net/problem/18409

import sys


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_single_str() -> str:
    return sys.stdin.readline().strip()


def solution(s: str):
    return len([*filter(lambda x: x in 'aeiou', [*s])])


def main():
    n = read_single_int()
    s = read_single_str()
    print(solution(s))


if __name__ == '__main__':
    main()
