# Title: 어려운 소인수 분해
# Link: https://www.acmicpc.net/problem/16536

import sys
import math

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def prime_sieve(size):
    sieve = [True for _ in range(size+1)]
    sieve[0], sieve[1] = False, False
    for i in range(2, int(math.sqrt(size))+1):
        if sieve[i] == False:
            continue
        for mul in range(i*i, size+1, i):
            sieve[mul] = False
    primes = []
    for i in range(size+1):
        if sieve[i]:
            primes.append(i)
    return primes


def get_prime_factors(n: int, primes: list):
    factors = []
    for p in primes:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            factors.append((p, count))
    
    for factor in factors:
        for _ in range(factor[1]):
            print(factor[0], end=' ')



def solution(n: int, ns: list):
    primes = prime_sieve(5000000)
    for num in ns:
        get_prime_factors(num, primes)
        print()


def main():
    n = read_single_int()
    ns = read_list_int()
    solution(n, ns)


if __name__ == '__main__':
    main()