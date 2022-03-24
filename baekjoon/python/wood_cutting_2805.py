# Title: 나무 자르기
# Link: https://www.acmicpc.net/problem/2805

import sys
import bisect

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def cut_woods(n: int, woods: list, height: int):
    i = bisect.bisect_right(woods, height)
    if i < n:
        return sum(woods[i:]) - (height * (n-i))
    return 0


def solution(n: int, want: int, woods: list):
    woods = sorted(woods)
    high = woods[-1]
    low = 0
    ans = 0

    while True:
        if high - low <= 1:
            break

        height = low + (high - low) // 2

        length = cut_woods(n, woods, height)

        if length < want:
            high = height
        elif length > want:
            low = height
            ans = height
        else:
            return height

    return ans


def main():
    n, m = read_list_int()
    woods = read_list_int()
    print(solution(n, m ,woods))


if __name__ == '__main__':
    main()