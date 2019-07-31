# Title: 배수와 약수
# Link: https://www.acmicpc.net/problem/5086

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a: int, b: int):
    if b % a == 0:
        return 'factor'
    elif a % b == 0:
        return 'multiple'
    return 'neither'


def main():
    while True:
        a, b = read_list_int()
        if a == 0 and b == 0:
            break
        print(solution(a, b))


if __name__ == '__main__':
    main()