# Title: 날짜 계산
# Link: https://www.acmicpc.net/problem/1476

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(e: int, s: int, m: int):
    ans = (532*13*e + 285*17*s + 420*10*m)%7980
    return 7980 if ans == 0 else ans


def main():
    e, s, m = read_list_int()
    print(solution(e, s, m))


if __name__ == '__main__':
    main()