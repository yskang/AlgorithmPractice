# Title: !밀비 급일
# Link: https://www.acmicpc.net/problem/11365

import sys


sys.setrecursionlimit(10 ** 6)

read_list_str = lambda: list(sys.stdin.readline().strip())


def solution(line: list):
    return ''.join(reversed(line))


def main():
    while True:
        line = read_list_str()
        if line != list('END'):
            print(solution(line))
        else:
            break


if __name__ == '__main__':
    main()