# Title: 골드바흐의 추측
# Link: https://www.acmicpc.net/problem/6588

import sys
import math

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def get_primes():
    ns = [True for i in range(1000001)]
    ns[0], ns[1] = False, False

    n = 2
    i = 2
    while n < math.sqrt(len(ns)-1):
        num = n*i
        while num < len(ns):
            ns[num] = False
            i += 1
            num = n*i
        j = n + 1
        while j < len(ns) and ns[j] == False:
            j += 1
        n = j
        i = 2

    return ns


def solution(n: int, primes: list, filtered: list):
    for prime_number, _ in filtered:
        if primes[n - prime_number]:
            return '{} = {} + {}'.format(n, prime_number, n-prime_number)
    return "Goldbach's conjecture is wrong."


def main():
    primes = get_primes()
    filtered = list(filter(lambda x: x[1] and x[0]%2==1 ,enumerate(primes)))
    while True:
        n = read_single_int()
        if n == 0:
            break
        print(solution(n, primes, filtered))


if __name__ == '__main__':
    main()
