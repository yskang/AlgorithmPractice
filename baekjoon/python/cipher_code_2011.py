# Title: 암호코드
# Link: https://www.acmicpc.net/problem/2011

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def solution(code: str):
    if len(code) == 1:
        if code == '0':
            return 0
        else:
            return 1

    d = [0 for _ in range(len(code)+2)]
    d[1] = 1
    d[2] = 2 if int(code[0:2]) <= 26 and int(code[1:2]) != 0 else 1

    for i in range(3, len(code)+1):
        if int(code[i-1:i]) != 0:
            d[i] += d[i-1]
        if int(code[i-2:i]) <= 26 and int(code[i-2:i-1]) != 0:
            d[i] += d[i-2]

    return d[len(code)] % 1000000


def main():
    code = read_single_str()
    print(solution(code))


if __name__ == '__main__':
    main()