# Title: Christmas
# Link: https://abc115.contest.atcoder.jp/tasks/abc115_d

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def f(n: int, x: int, a: list, p: list):
    if n == 0 and x == 0:
        return 0
    elif n == 0:
        return 1
    elif x == 1:
        return 0
    elif 1 < x <= 1 + a[n-1]:
        return f(n-1, x-1, a, p)
    elif x == 2 + a[n-1]:
        return p[n-1] + 1
    elif 2+a[n-1] < x <= 2+2*a[n-1]:
        return p[n-1]+1+f(n-1, x-(2+a[n-1]), a, p)
    elif x == 3 + 2*a[n-1]:
        return 2*p[n-1]+1


def solution(n: int, x: int):
    a = [1] + [0]*n
    p = [1] + [0]*n

    for i in range(1, n+1):
        a[i] = 2*a[i-1] + 3
        p[i] = 2*p[i-1] + 1
    
    return f(n, x, a, p)



def main():
    n, x = read_list_int()
    print(solution(n, x))


if __name__ == '__main__':
    main()