# Title: 중앙 이동 알고리즘
# Link: https://www.acmicpc.net/problem/2930

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    ans = 3
    for i in range(n-1):
        ans = ans * 2 - 1
    return ans*ans


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()