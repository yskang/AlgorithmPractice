# Title: -2 진수
# Link: https://www.acmicpc.net/problem/-2089

import sys

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    ans = ''
    if n == 0:
        return '0'
    while n != 0:
        d, r = divmod(n, -2)
        if r == 0:
            ans += '0'
            n = d
        else:
            ans += str(r+2)
            n = d+1
    return ''.join(list(reversed(ans)))


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()