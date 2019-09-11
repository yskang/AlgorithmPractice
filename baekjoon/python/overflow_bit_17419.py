# Title: 비트가 넘쳐흘러
# Link: https://www.acmicpc.net/problem/17419

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_single_str = lambda: sys.stdin.readline().strip()


def solution(n: int, num: str):
    return num.count('1')


def main():
    n = read_single_int()
    num = read_single_str()
    print(solution(n, num))


if __name__ == '__main__':
    main()