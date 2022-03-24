# Title: 서로 다른 부분 문자열의 개수
# Link: https://www.acmicpc.net/problem/11478

import sys


sys.setrecursionlimit(10 ** 6)


read_single_str = lambda: sys.stdin.readline().strip()


def get_substring(s: str):
    pool = set()

    for start in range(len(s)):
        for end in range(start+1, len(s)+1):
            pool.add(s[start:end])

    return len(pool)


def main():
    S = read_single_str()
    print(get_substring(S))


if __name__ == '__main__':
    main()