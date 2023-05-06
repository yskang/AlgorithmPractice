# Title: 소수의 합
# Link: https://www.acmicpc.net/problem/27519

import sys


MOD = 10**9+7


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def sieve_of_eratosthenes(n: int) -> list:
    primes = [True for _ in range(n+1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes


def main():
    t = read_single_int()
    questions = []
    for _ in range(t):
        questions.append(read_single_int())
    max_question = max(questions)

    prime_check = sieve_of_eratosthenes(max_question)
    primes = [i for i in range(max_question+1) if prime_check[i]]

    nums = [0 for _ in range(max_question+1)]
    for prime in primes:
        nums[prime] = (nums[prime] + 1) % MOD
        for i in range(prime+1, len(nums)):
            nums[i] = (nums[i] % MOD + nums[i-prime] % MOD) % MOD
    for question in questions:
        print(nums[question])


if __name__ == '__main__':
    main()