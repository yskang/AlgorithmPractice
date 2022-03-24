# Title: 라쿤이 정보섬에 올라온 이유
# Link: https://www.acmicpc.net/problem/17133

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(num_raccoon: int, num_candy: int, k: int, raccoons: list, sugar_candies: list, a: int):
    while True:
        for raccoon in raccoons:
            

def main():
    n, m, k, r = read_list_int()
    ns = read_list_int()
    ms = read_list_int()
    a = read_single_int()
    print(solution(n, m, k, r, ns, ms, a))


if __name__ == '__main__':
    main()