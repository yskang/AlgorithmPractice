# Title: 다항 계수
# Link: https://www.acmicpc.net/problem/16725

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

MOD = 1000000009


def solution(a: int, n: int, k: int):
    window_size = a+1
    a_list = [1] * (a+1) 
    temp = [1] * (a+1)
    for _ in range(n-1):
        temp = [0 for i in range(window_size)]
        temp[0] = a_list[0]

        for i in range(1, window_size):
            temp[i] = (temp[i-1] + (a_list[i] % MOD)) % MOD
        
        for i in range(window_size, len(a_list)+window_size-1):
            temp.append((temp[-1]-a_list[i-window_size] + (a_list[i] if i < len(a_list) else 0))%MOD )
        a_list = temp
    return temp[k]


def main():
    n, m, k = read_list_int()
    print(solution(n, m, k))


if __name__ == '__main__':
    main()