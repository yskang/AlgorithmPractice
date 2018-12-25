# Title: PPAP
# Link: https://www.acmicpc.net/problem/16120

import sys
import collections
import random

sys.setrecursionlimit(10 ** 6)

read_list_str = lambda: list(sys.stdin.readline().strip())


def solution(s: list):
    stack = []
    for c in s:
        stack.append(c)
        if stack[len(stack)-4 if len(stack)-4 >= 0 else len(stack):len(stack)] == ['P', 'P', 'A', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()

    if stack == ['P']:
        return 'PPAP'
    return 'NP'


def main():
    s = read_list_str()
    print(solution(s))


if __name__ == '__main__':
    main()