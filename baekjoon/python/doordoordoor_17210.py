# Title: 문문문
# Link: https://www.acmicpc.net/problem/17210

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, start: int):
    if n > 5:
        return 'Love is open door'
    ans = []
    s = False if start else True
    for i in range(n-1):
        ans.append(s)
        s = not s
    ans = list(map(lambda x: '1' if x else '0', ans))
    return '\n'.join(ans)


def main():
    n = read_single_int()
    start = read_single_int()
    print(solution(n, start))


if __name__ == '__main__':
    main()