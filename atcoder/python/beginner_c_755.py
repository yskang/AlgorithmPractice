# Title: count Shichi-Go-San numbers under N
# Link: https://abc114.contest.atcoder.jp/tasks/abc114_c

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def dfs(s: str, n: int, count: list):
    if int(s) > n:
        return
    if s.count('3') >= 1 and s.count('5') >= 1 and s.count('7') >= 1:
        count[0] += 1
    
    dfs(s+'3', n, count)
    dfs(s+'5', n, count)
    dfs(s+'7', n, count)


def solution(n: int):
    count = [0]
    dfs('0', n, count)
    return count[0]


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()