# Title: 두 용액
# Link: https://www.acmicpc.net/problem/2470

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, fs: list):
    fs = sorted(fs, key=lambda f: abs(f))
    min_val = 2*10**10
    ans = []
    prev = fs[0]
    for f in fs[1:]:
        if abs(prev + f) < min_val:
            min_val = abs(prev + f)
            ans = [prev, f]
        prev = f
    return ' '.join(map(str, sorted(ans)))


def main():
    n = read_single_int()
    fs = read_list_int()
    print(solution(n, fs))


if __name__ == '__main__':
    main()