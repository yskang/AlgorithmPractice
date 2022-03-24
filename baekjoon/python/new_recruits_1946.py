# Title: 신입 사원
# Link: https://www.acmicpc.net/problem/1946

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list):
    count = 1
    prev = ns[1]
    for i in range(2, n+1):
        if ns[i] < prev:
            count += 1
            prev = ns[i]
            if ns[i] == 1:
                break

    return count


def main():
    t = read_single_int()
    for _ in range(t):
        n = read_single_int()
        ns = [0 for _ in range(n+1)]
        for _ in range(n):
            a, b = read_list_int()
            ns[a] = b
        print(solution(n, ns))


if __name__ == '__main__':
    main()