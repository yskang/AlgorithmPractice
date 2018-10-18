# Title: 진법 변환 2
# Link: https://www.acmicpc.net/problem/11005

import sys
import string

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

nums = [str(i) for i in range(10)] + list(string.ascii_uppercase)

def solution(n: int, b: int):
    ans = []

    d = -1
    while d != 0:
        (d, r) = divmod(n, b)
        ans.append(nums[r])
        n = d

    return ''.join(list(reversed(ans)))


def main():
    n, b = read_list_int()
    print(solution(n, b))


if __name__ == '__main__':
    main()