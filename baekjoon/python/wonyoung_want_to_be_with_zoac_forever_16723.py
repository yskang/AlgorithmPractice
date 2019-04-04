# Title: 원영이는 ZOAC과 영원하고 싶다
# Link: https://www.acmicpc.net/problem/16723

import sys
import math


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    s = 0
    bin_num = bin(n)[2:]
    sums = [2, 4]

    for i in range(2, len(bin_num)+1):
        sums.append(sums[i-1]*2 + pow(2, i-1))

    for i in range(1, len(sums)):
        sums[i] += sums[i-1]

    for i, d in enumerate(reversed(bin_num)):
        if d == '1':
            s += sums[i]
    return s


def solution_bf(n: int):
    ans = 0
    for i in range(1, n+1):
        num_gifts = 2*i

        f = int(math.log2(num_gifts))
        attend = pow(2, f)

        while True:
            if num_gifts % attend == 0:
                ans += attend
                break
            attend //= 2


    return ans


def solution_bf2(n: int):
    sum = n*2
    base = 2
    while base <= n:
        sum += (n//base) * base
        base *= 2
    return sum


def main():
    n = read_single_int()
    print(solution(n), solution_bf2(n))


if __name__ == '__main__':
    main()