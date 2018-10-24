# Title: 숫자 카드
# Link: https://www.acmicpc.net/problem/10815

import sys
import collections

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list, m: int, ms: list):
    num_dict = collections.defaultdict(lambda: False)

    for num in ns:
        num_dict[num] = True
    
    for i in ms:
        if num_dict[i]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    return


def main():
    n = read_single_int()
    ns = read_list_int()
    m = read_single_int()
    ms = read_list_int()
    solution(n, ns, m, ms)


if __name__ == '__main__':
    main()