# Title: 최댓값
# Link: https://www.acmicpc.net/problem/2562

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(ns: list):
    i, n = max(enumerate(ns), key=lambda x: x[1])
    return '{}\n{}'.format(n, i+1)

def main():
    nums = []
    for _ in range(9):
        nums.append(read_single_int())
    print(solution(nums))


if __name__ == '__main__':
    main()