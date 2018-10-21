# Title: 소인수분해
# Link: https://www.acmicpc.net/problem/11653

import sys
import math

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    ans = []

    p = 2
    while p*p <= n:
        while True:
            d, r = divmod(n, p)
            if r == 0:
                ans.append(p)
                n = d
            else:
                break
        p += 1

    if n != 1:
        ans.append(n)

    return '\n'.join(map(str, ans))


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()