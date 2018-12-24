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
        if stack[len(stack)-4 if len(stack)-4 >= 0 else 0:len(stack)] == ['P', 'P', 'A', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()

    stack = ''.join(stack)
    if stack.count('A') == 0:
        return 'PPAP'
    return 'NP'


def main():
    # s = read_list_str()
    while True:
        s = 'PPAPA'
        for i in range(50):
            k = random.randint(0, len(s)-1)
            if s[k] == 'P':
                s = s[:k] + 'PPAP' + s[k+1:]
        
        if solution(list(s)) == 'PPAP':
            print(s)
            break


if __name__ == '__main__':
    main()