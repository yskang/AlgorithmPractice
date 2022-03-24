# Title: 귀찮음
# Link: https://www.acmicpc.net/problem/16208

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, sticks: list):
    ans = 0

    len_stick = sum(sticks)
    sticks = sorted(sticks)

    for stick in sticks:
        len_stick -= stick
        ans += stick * len_stick

    return ans


def main():
    n = read_single_int()
    sticks = read_list_int()
    print(solution(n, sticks))


if __name__ == '__main__':
    main()