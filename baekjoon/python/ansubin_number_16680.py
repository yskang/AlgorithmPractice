# Title: 안수빈수
# Link: https://www.acmicpc.net/problem/16680

import sys
import random

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())

max_num = pow(10, 18)

def solution(n):
    v, d = divmod(max_num, n)
    x = max_num-d
    a = 1
    while True:
        s = sum(map(int, list(str(x))))
        if s % 2 == 1:
            return x
        x -= (n*a)
        a = 2*a

def main():
    t = read_single_int()
    for _ in range(t):
        n = read_single_int()
        print(solution(n))
    # while True:
    #     n = random.randint(1, 100000000)
    #     print('{} : {}'.format(n, solution(n)))

if __name__ == '__main__':
    main()