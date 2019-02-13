# Title: 어려운 소인수 분해
# Link: https://www.acmicpc.net/problem/16536

import sys
import math

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def prime_sieve(sieveSize):
    sieve = [True] * (sieveSize+1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2,int(math.sqrt(sieveSize))+1):
        if sieve[i] == False:
            continue
        for pointer in range(i**2, sieveSize+1, i):
            sieve[pointer] = False
    primes = []
    for i in range(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)
    return primes


def get_prime_factors(n: int):
    primelist = prime_sieve(n)
    factors = []
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            factors.append((p, count))
    
    ans = []
    for factor in factors:
        for _ in range(factor[1]):
            ans.append(str(factor[0]))

    return ' '.join(ans)


def solution(n: int, ns: list):
    for num in ns:
        facts = get_prime_factors(num)
        print(facts)


def main():
    n = read_single_int()
    ns = read_list_int()
    solution(n, ns)


if __name__ == '__main__':
    main()