# https://www.acmicpc.net/problem/2839
import sys
import math

N = int(sys.stdin.readline())

def make_number(number, coins, total):
    min_count = sys.maxsize

    for coin in coins:
        if 0 <= number-coin < len(total) and coin < len(total):
            count = total[number-coin] + total[coin]
            if 0 < count < min_count:
                min_count = count
    
    total[number] = min_count
    return min_count

def coin_change(coins, amount):
    if amount is 0:
        return 0
    
    total = [0] * (amount+1)

    for coin in coins:
        if coin >= len(total):
            continue
        total[coin] = 1
    
    total[0] = 0
    for i in range(1, amount+1):
        total[i] = make_number(i, coins, total)
    
    if total[amount] is sys.maxsize:
        return -1
    return total[amount]

print(coin_change([3,5], N))

