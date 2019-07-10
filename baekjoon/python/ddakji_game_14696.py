# Title: 딱지놀이
# Link: https://www.acmicpc.net/problem/14696

import sys
from collections import defaultdict


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())

sys.setrecursionlimit(10 ** 6)


def solution(a_card: list, b_card: list):
    a_dic = defaultdict(lambda:0)
    b_dic = defaultdict(lambda:0)
    for a in a_card:
        a_dic[a] += 1
    for b in b_card:
        b_dic[b] += 1

    for i in range(4, 0, -1):
        if a_dic[i] > b_dic[i]:
            return 'A'
        elif a_dic[i] < b_dic[i]:
            return 'B'
    return 'D'



def main():
    n = read_single_int()
    for _ in range(n):
        a = read_list_int()
        b = read_list_int()
        print(solution(a[1:], b[1:]))


if __name__ == '__main__':
    main()