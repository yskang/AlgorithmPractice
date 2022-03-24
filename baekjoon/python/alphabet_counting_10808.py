# Title: 알파벳 개수
# Link: https://www.acmicpc.net/problem/10808

import sys


sys.setrecursionlimit(10 ** 6)


read_single_str = lambda: sys.stdin.readline().strip()


def solution(s: str):
    a = ord('a')
    ans = [0 for _ in range(26)]
    for c in s:
        ans[ord(c)-a] += 1
    return ans


def main():
    s = read_single_str()
    print(' '.join(map(str, solution(s))))


if __name__ == '__main__':
    main()