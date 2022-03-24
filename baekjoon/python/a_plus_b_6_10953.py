# Title: A+B - 6
# Link: https://www.acmicpc.net/problem/10953

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_single_str = lambda: sys.stdin.readline().strip()

def solution(a: int, b: int):
    return a+b


def main():
    T = read_single_int()
    for _ in range(T):
        A, B = list(map(int, read_single_str().split(',')))
        print(solution(A, B))


if __name__ == '__main__':
    main()