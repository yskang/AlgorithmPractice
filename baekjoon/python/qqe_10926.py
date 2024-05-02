# Title: ??!
# Link: https://www.acmicpc.net/problem/10926

import sys


def read_single_str() -> str:
    return sys.stdin.readline().strip()


def solution(id: str) -> str:
    return id + '??!'


def main():
    id = read_single_str()
    print(solution(id))


if __name__ == '__main__':
    main()
