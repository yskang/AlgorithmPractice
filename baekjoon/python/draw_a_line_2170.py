# Title: 선 긋기
# Link: https://www.acmicpc.net/problem/2170

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

INF = 10*10

def solution(n: int, lines: list):
    lines = sorted(lines, key = lambda x: x[0])

    ans = 0
    left = lines[0][0]
    right = lines[0][1]
    for s, e in lines[1:]:
        if left <= s <= right:
            right = max(right, e)
        else:
            ans += right-left
            left = s
            right = e
    ans += right-left
    return ans


def main():
    n = read_single_int()
    lines = []
    for _ in range(n):
        lines.append(read_list_int())
    print(solution(n, lines))


if __name__ == '__main__':
    main()