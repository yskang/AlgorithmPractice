# Title: 팽귄추락대책위원회
# Link: https://www.acmicpc.net/problem/18228

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

min_int = 10**10

def solution(n: int, ices: list):
    left_min, right_min = min_int, min_int
    left_found = False
    for force in ices:
        if left_found == False:
            if force == -1:
                left_found = True
                continue
            if force < left_min:
                left_min = force
        else:
            if force < right_min:
                right_min = force
    return left_min+right_min


def main():
    n = read_single_int()
    ices = read_list_int()
    print(solution(n, ices))


if __name__ == '__main__':
    main()