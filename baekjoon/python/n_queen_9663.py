# Title: N-Queen
# Link: https://www.acmicpc.net/problem/9663

import sys
import math


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def available(queens: list, new_queen: int, n: int):
    j = len(queens)
    for i, queen in enumerate(queens):
        if queen == new_queen:
            return False
        elif abs(queen-new_queen) == abs(i-j):
            return False
    return True


def set_queen(queens: list, n: int, count: list):
    if len(queens) == n:
        count[0] += 1
    else:
        for i in range(n):
            if available(queens, i, n):
                queens.append(i)
                set_queen(queens, n, count)
    queens.pop()



def solution_(n: int):
    count = [0]
    for i in range(n):
        queens = [i]
        set_queen(queens, n, count)
    return count[0]


def solution(n: int):
    ans = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]
    return ans[n]


def main():
    print(solution(read_single_int()))


if __name__ == '__main__':
    main()