# Title: 동물원
# Link: https://www.acmicpc.net/problem/1309

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n):
    d = [1, 1, 1]
    d2 = [0, 0, 0]
    for _ in range(1, n):
        d2[0] = d[0] + d[1] + d[2]
        d2[1] = d[0] + d[2]
        d2[2] = d[0] + d[1]
        d2, d = d, d2
    return sum(d)%9901


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()