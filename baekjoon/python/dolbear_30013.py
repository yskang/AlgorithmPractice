# Title: 돌베어 법칙
# Link: https://www.acmicpc.net/problem/30013

import sys
import math


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_single_str() -> str:
    return sys.stdin.readline().strip()


def check(p: int, ks: list, xs: set, min_num: int, f: int) -> int:
    count = 0
    first = f
    while True:
        # 1. find first '#', count += 1
        for i in range(first, len(ks)):
            if ks[i] == '#':
                count += 1
                first = i
                break
        else:
            break

        if count >= min_num:
            return count

        # 2. remove from first position to end
        for i in range(first, len(ks), p):
            if ks[i] == '#':
                ks[i] = '.'
                xs.add(i)
            else:
                break

    return count


def solution(n: int, ks: list) -> int:
    xs = set()
    ps = [i for i in range(1, n)]
    min_num = 10**10

    first = 0
    for i in range(len(ks)):
        if ks[i] == '#':
            first = i
            break

    for p in ps:
        num = check(p, ks, xs, min_num, first)
        if num < min_num:
            min_num = num
        while xs:
            ks[xs.pop()] = '#'

    return min_num


def main():
    print(solution(read_single_int(), list(read_single_str())))


if __name__ == '__main__':
    main()