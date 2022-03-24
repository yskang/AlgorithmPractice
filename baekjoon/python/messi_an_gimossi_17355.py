# Title: Messi An-Gimossi
# Link: https://www.acmicpc.net/problem/17355

import sys
from collections import defaultdict
from math import sqrt

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

MOD = 1000000007


def prime_factorization(n: int, primes: defaultdict, cache: list):
    num = n
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            primes[i] += 1
            factors.append(i)
    if n > 1:
        primes[n] += 1
        factors.append(n)
    cache[num] = factors


def solution(ps: list):
    ups = defaultdict(lambda: 0)
    downs = defaultdict(lambda: 0)
    cache = defaultdict(lambda: [])

    for a, b in ps:
        if cache[b-a]:
            for prime in cache[b-a]:
                ups[prime] += 1
        else:
            prime_factorization(b-a, ups, cache)
        
        if cache[b]:
            for prime in cache[b]:
                downs[prime] += 1
        else:
            prime_factorization(b, downs, cache)

    for prime in downs:
        if ups[prime] >= downs[prime]:
            ups[prime] -= downs[prime]
            downs[prime] = 0
        else:
            downs[prime] -= ups[prime]
            ups[prime] = 0

    up, down = 1, 1
    for prime in ups:
        for _ in range(ups[prime]):
            up = (up * (prime % MOD)) % MOD
    for prime in downs:
        for _ in range(downs[prime]):
            down = (down * (prime % MOD)) % MOD

    return '{} {}'.format(up, down)


def main():
    n = read_single_int()
    ps = []
    for _ in range(n):
        ps.append(read_list_int())
    print(solution(ps))


if __name__ == '__main__':
    main()