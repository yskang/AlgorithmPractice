# Title: GCD(n, k) = 1
# Link: https://www.acmicpc.net/problem/11698:

import sys
import math

sys.setrecursionlimit(10 ** 6)

def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def get_primes_under(n):
    ns = {k:True for k in range(2, n+1) }
    for num in range(2, int(math.sqrt(n))+1):
        if num in ns:
            i = 2
            while num*i <= n:
                if num*i in ns:
                    del ns[num*i]
                i += 1
    return ns.keys()


def get_prime_factors(n, primes):
    factors = []
    for p in primes:
        if n % p == 0:
            factors.append(p)
    return factors


def num_gcd(n):
    primes = get_primes_under(n)
    factors = get_prime_factors(n, primes)
    up, down = 1, 1
    for f in factors:
        up *= (f-1)
        down *= f
    return n * up // down


if __name__ == '__main__':
    #n = read_single_int()
    for i in range(2, 20000):
        print('{}: {}'.format(i, num_gcd(i)))

