# Title: A+B - 4
# Link: https://www.acmicpc.net/problem/10951

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def solution(a: int, b: int):
    return a+b


def main():
    while True:
        try:
            A, B = read_list_int()
        except:
            break
        print(solution(A, B))


if __name__ == '__main__':
    main()