import sys
from functools import reduce

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    factorial = list(str(reduce(lambda x, y: x * y, [z for z in range(1, n+1)], 1)))
    zero = 0
    while factorial[-1] == "0":
        factorial.pop()
        zero += 1
    print(zero)