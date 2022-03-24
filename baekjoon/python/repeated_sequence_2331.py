# Title: 반복수열
# Link: https://www.acmicpc.net/problem/2331

import sys
import collections

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_number(n: int, p: int):
    ans = 0
    s = str(n)
    for c in s:
        ans += int(c) ** p
    return ans


def solution(a: int, p: int):
    d = [a]
    pool = collections.defaultdict(lambda: -1)
    pool[a] = 0
    while True:
        num = get_number(d[-1], p)
        if pool[num] == -1:
            pool[num] = len(d)
            d.append(num)
            continue
        return pool[num]


def main():
    a, p = read_list_int()
    print(solution(a, p))


if __name__ == '__main__':
    main()