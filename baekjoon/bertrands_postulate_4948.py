# https://www.acmicpc.net/problem/4948

import sys

import math


def count_prime_number(n):
    ns = {x: x for x in range(n+1, 2*n+1)}
    for k in range(2, int(math.sqrt(2*n+1)+1)):
        i = round((n+1)/k)
        if i == 1:
            i = 2
        while k*i < 2*n+1:
            if k*i in ns:
                del ns[k*i]
            i += 1

    return len(ns)


def prim_numbers(ins):
    maximum = max(ins)
    nums = [True] * ((maximum * 2) + 2)
    last = int(math.sqrt(len(nums)-1))
    for seed in range(2, last+1):
        v = 2
        while True:
            if seed*v < len(nums):
                nums[seed*v] = False
                v += 1
            else:
                break
    for n in ins:
        count = 0
        for i in range(n+1, 2*n+1):
            if nums[i]:
                count += 1
        print(count)


if __name__ == "__main__":
    ns = []
    while True:
        N = int(sys.stdin.readline())
        if N == 0:
            break
        ns.append(N)

    prim_numbers(ns)

