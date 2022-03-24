# https://www.acmicpc.net/problem/9020
import math
import sys

def get_partitions(ins):
    maximum = max(ins)
    nums = [True] * (maximum + 2)
    last = int(math.sqrt(len(nums)-1))
    for seed in range(2, last+1):
        v = 2
        while True:
            if seed*v < len(nums):
                nums[seed*v] = False
                v += 1
            else:
                break

    primes = {}
    primes_list = []
    for n in range(2, len(nums)):
        if nums[n]:
            primes[n] = n
            primes_list.append(n)

    for num in ins:
        candidates = []
        for prime in primes_list:
            if prime > num / 2:
                break
            if num - prime in primes:
                candidates.append((prime, num-prime))
        print("{} {}".format(candidates[-1][0], candidates[-1][1]))



if __name__ == "__main__":
    T = int(input())
    nums = []
    for i in range(T):
        nums.append(int(sys.stdin.readline()))
    get_partitions(nums)
