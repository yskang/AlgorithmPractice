# Title: 조세퍼스 문제 2
# Link: https://www.acmicpc.net/problem/1168

import sys
import collections


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int):
    ans = []
    d = collections.deque([i for i in range(1, n+1)])
    while len(d) > 0:
        d.rotate(-(m-1))
        ans.append(d.popleft())
    
    return '<{}>'.format(', '.join(map(str, ans)))


def main():
    n, m = read_list_int()
    print(solution(n, m))


if __name__ == '__main__':
    main()