# Title: PPAP
# Link: https://www.acmicpc.net/problem/16120

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def solution(s: str):
    while True:
        s = s.replace('PPAP', 'P', -1)
        if s.count('PPAP') == 1 and len(s) == 4:
            return 'PPAP'
        elif s.count('PPAP') == 0 and len(s) > 0:
            return 'NP'
    


def main():
    s = read_single_str()
    print(solution(s))


if __name__ == '__main__':
    main()