# Title: 전구 길만 걷자
# Link: https://www.acmicpc.net/problem/17359

import sys
from itertools import permutations
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_single_str = lambda: sys.stdin.readline().strip()


def solution(n: int, bulbs: list):
    count = 0
    bulb_dic = defaultdict(lambda: 0)

    for bulb in bulbs:
        count += bulb.count('01')
        count += bulb.count('10')
        bulb_dic[(int(bulb[0]), int(bulb[-1]))] += 1
    
    if bulb_dic[(0, 0)] == n or bulb_dic[(1, 1)] == n:
        return count
    elif bulb_dic[(0, 0)] + bulb_dic[(1, 1)] == n:
        return count + 1
    else:
        d = abs(bulb_dic[(0, 1)] - bulb_dic[(1, 0)])
        if d == 1 or d == 0:
            return count
        return count + d - 1


def main():
    n = read_single_int()
    bulbs = []
    for _ in range(n):
        bulbs.append(read_single_str())
    print(solution(n, bulbs))


if __name__ == '__main__':
    main()