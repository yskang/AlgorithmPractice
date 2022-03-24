# Title: 기프티콘이 흘러넘쳐
# Link: https://www.acmicpc.net/problem/17420

import sys
from math import ceil
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, validities: list, uses: list):
    count = 0
    giftcons = defaultdict(lambda: [])

    for i in range(n):
        giftcons[uses[i]].append(validities[i])
    
    days = sorted(giftcons.keys())

    prev_validity = -1
    for use in days:
        day_max = -1
        for validity in giftcons[use]:
            if validity < use:
                extend = ceil((use-validity)/30)
                count += extend
                validity += extend*30
            if validity < prev_validity:
                extend = ceil((prev_validity-validity)/30)
                count += extend
                validity += extend*30
            day_max = max(day_max, validity)
        prev_validity = day_max

    return count
    

def main():
    n = read_single_int()
    a = read_list_int()
    b = read_list_int()
    print(solution(n, a, b))


if __name__ == '__main__':
    main()