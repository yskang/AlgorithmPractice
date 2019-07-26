# Title: 직각삼각형
# Link: https://www.acmicpc.net/problem/4153

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(a, b, c):
    a = a*a
    b = b*b
    c = c*c
    if a == b+c or b == a+c or c == a+b:
        return 'right'
    return 'wrong'


def main():
    while True:
        a, b, c = read_list_int()
        if a == b == c == 0:
            break
        print(solution(a, b, c))
    


if __name__ == '__main__':
    main()