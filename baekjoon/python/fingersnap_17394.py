# Title: 핑거스냅
# Link: https://www.acmicpc.net/problem/17394

import sys
from collections import deque, defaultdict


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def sieve_of_eratosthenes(n: int) -> list:
    primes = [True for _ in range(n+1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes


def solution(n: int, a: int, b: int, is_prime: list) -> int:
    visited = [False for _ in range(1000000+1)]

    no_prime = True
    for i in range(a, b+1):
        if is_prime[i]:
            no_prime = False
            break
    if no_prime:
        return -1

    q = deque()
    q.append((n, 0))
    visited[n] = True

    while q:
        num, count = q.popleft()

        if a <= num <= b and is_prime[num]:
            return count

        new_nums = [num//2, num//3, num+1, num-1]
        for new_num in new_nums:
            if 0 <= new_num <= 1000000 and not visited[new_num]:
                visited[new_num] = True
                q.append((new_num, count+1))

    return -1


def main():
    is_prime = sieve_of_eratosthenes(10**5)
    t = read_single_int()
    for _ in range(t):
        n, a, b = read_list_int()
        print(solution(n, a, b, is_prime))


if __name__ == '__main__':
    main()