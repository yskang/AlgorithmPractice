# Title: 겨울왕국 티켓 예매
# Link: https://www.acmicpc.net/problem/18247

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int):
    #n = row, m = column
    # l = 12
    x = 0
    for r in range(n):
        for c in range(m):
            x += 1
            if r == 11 and c == 3:
                return x
    return -1


def main():
    t = read_single_int()
    for _ in range(t):
        n, m = read_list_int()
        print(solution(n, m))


if __name__ == '__main__':
    main()