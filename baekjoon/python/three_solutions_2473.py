# Title: 세 용액
# Link: https://www.acmicpc.net/problem/2473

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, fs: list):
    fs = sorted(fs)
    ans = []
    min_val = 2*10**10
    for first in range(n-2):
        third = n-1
        for second in range(first+1, n-1):
            while True:
                if third <= second:
                    break
                if fs[first] + fs[second] + fs[third] <= 0:
                    break
                third -= 1
            if third < second:
                break
            for cand in range(third-1, third+2):
                if cand <= second or cand >= n:
                    continue
                tmp = abs(fs[first] + fs[second] + fs[cand])
                if min_val > tmp:
                    min_val = tmp
                    ans = [fs[first], fs[second], fs[cand]]
    return '{} {} {}'.format(*ans)

def main():
    n =  read_single_int()
    fs = read_list_int()
    print(solution(n, fs))


if __name__ == '__main__':
    main()