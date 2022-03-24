# Title: 잃어버린 괄호
# Link: https://www.acmicpc.net/problem/brace

import sys


sys.setrecursionlimit(10 ** 6)


read_single_str = lambda: sys.stdin.readline().strip()


def solution(eq: str):
    eq = eq.replace('+', ',+').replace('-', ',-')
    elements = eq.split(',')
    elements = list(map(int, elements))
    ans = 0
    minus = False
    for e in elements:
        if not minus:
            if e >= 0:
                ans += e
            else:
                ans += e
                minus = True
        else:
            ans -= abs(e)
    return ans


def main():
    eq = read_single_str()
    print(solution(eq))


if __name__ == '__main__':
    main()