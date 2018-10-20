# Title: Base Conversion
# Link: https://www.acmicpc.net/problem/11576

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(a: int, b: int, m: int, ns: list):
    ans = []
    
    a_10 = 0
    for i, n in enumerate(ns, 1):
        a_10 += n * pow(a, m-i)

    if a_10 == 0:
        return '0'

    while a_10 != 0:
        d, r = divmod(a_10, b)
        ans.append(r)
        a_10 = d

    return ' '.join(map(str, (reversed(ans))))


def main():
    a, b = read_list_int()
    m = read_single_int()
    ns = read_list_int()
    print(solution(a, b, m, ns))


if __name__ == '__main__':
    main()