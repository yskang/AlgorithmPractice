# Title: N과 M (3)
# Link: https://www.acmicpc.net/problem/15651

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int):
    ans = [1 for _ in range(m)]
    print(*ans)
    while True:

        for i in range(m-1, -1, -1):
            if ans[i] < n:
                ans[i] += 1
                break
            else:
                ans[i] = 1
                if i == 0:
                    return
        print(*ans)


def main():
    n, m = read_list_int()
    solution(n, m)


if __name__ == '__main__':
    main()