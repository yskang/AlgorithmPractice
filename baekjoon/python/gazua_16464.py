# Title: 가주아
# Link: https://www.acmicpc.net/problem/16464

import sys
import math

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(k: int):
    if math.log2(k).is_integer():
        return 'GoHanGang'
    return 'Gazua'


def main():
    t = read_single_int()
    for _ in range(t):
        print(solution(read_single_int()))

if __name__ == '__main__':
    main()