# Title: 숫자 숏코딩
# Link: https://www.acmicpc.net/problem/29762

import sys
import math
from collections import defaultdict


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def primeFactors(n):
    ans = defaultdict(lambda: 0)
    while n % 2 == 0:
        ans[2] += 1
        n = n // 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            ans[i] += 1
            n = n // i
    if n > 2:
        ans[n] += 1
    return ans


def solution(n: int):
    if n <= 999:
        return n
    ans = []
    factors = primeFactors(n)
    print(factors)

    return ' '.join(ans)


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()