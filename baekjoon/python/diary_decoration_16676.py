# Title: 근우의 다이어리 꾸미기
# Link: https://www.acmicpc.net/problem/16676

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    l = len(str(n))
    if l == 1:
        return 1
    ones_str = '1'*l
    ones = int(ones_str)
    if n >= ones:
        return l
    return l-1


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()