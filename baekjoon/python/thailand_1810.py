# Title: 1998년생인 내가 태국에서는 2541년생?!
# Link: https://www.acmicpc.net/problem/1810

import sys


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def solution(y: int) -> int:
    return (y - 543)


def main():
    y = read_single_int()
    print(solution(y))


if __name__ == '__main__':
    main()