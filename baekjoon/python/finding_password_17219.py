# Title: 비밀번호 찾기
# Link: https://www.acmicpc.net/problem/17219

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_words = lambda: sys.stdin.readline().strip().split(' ')
read_single_str = lambda: sys.stdin.readline().strip()


def solution():
    pass


def main():
    n, m = read_list_int()
    pass_dic = defaultdict()
    for _ in range(n):
        addr, psswd = read_list_words()
        pass_dic[addr] = psswd
    for _ in range(m):
        site = read_single_str()
        print(pass_dic[site])


if __name__ == '__main__':
    main()