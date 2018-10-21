# Title: 소인수분해
# Link: https://www.acmicpc.net/problem/11653

import sys
import math

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def get_primes_under(n: int):
    ns = [True for _ in range(n+1)]
    ns[0], ns[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if ns[i]:
            for j in range(i+i, n+1, i):
                ns[j] = False
    return ns


def solution(n: int, primes: list):
    ans = []
    i = 0
    while n != 1:
        while True:
            d, r = divmod(n, primes[i][0])
            if r == 0:
                ans.append(primes[i][0])
                n = d
                break
            else:
                i += 1

    return '\n'.join(map(str, ans))


def main():
    n = read_single_int()
    primes = list(filter(lambda x: x[1] ,enumerate(get_primes_under(n))))
    print(solution(n, primes))


if __name__ == '__main__':
    main()