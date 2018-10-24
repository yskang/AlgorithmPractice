# Title: 수 찾기
# Link: https://www.acmicpc.net/problem/1920

import sys
import collections


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list, m: int, ms: list):
    num_dict = collections.defaultdict(lambda: False)
    for num in ns:
        num_dict[num] =  True
    for num in ms:
        if num_dict[num]:
            print(1)
        else:
            print(0)


def main():
    n = read_single_int()
    ns = read_list_int()
    m = read_single_int()
    ms = read_list_int()
    solution(n, ns, m, ms)


if __name__ == '__main__':
    main()