import sys
from functools import reduce
 
rl = lambda:sys.stdin.readline()
numOfNums = int(rl())
 
def isPrime(n):
    if n == 1 : return 0
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return 0
    return 1
 
print(reduce(lambda x, y: x + y, map(isPrime, list(map(int, rl().split(' '))))))