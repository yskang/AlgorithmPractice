# Title: 명령 프롬프트
# Link: https://www.acmicpc.net/problem/1032

import sys


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_single_str() -> str:
    return sys.stdin.readline().strip()


def solution(n: int, words: list):
    ans = list(words[0])
    for word in words[1:]:
        for i, c in enumerate(word):
            if ans[i] != c:
                ans[i] = '?'
    return ''.join(ans)


def main():
    n = read_single_int()
    words = []
    for _ in range(n):
        words.append(read_single_str())
    print(solution(n, words))


if __name__ == '__main__':
    main()