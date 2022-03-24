# Title: 계단 수
# Link: https://www.acmicpc.net/problem/1562

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


DIV = 1000000000


def get_number(pos: int, val: int, state: int, dp: list):
    if val < 0 or val > 9:
        return 0
    
    if pos == 1:
        if (state | (1<<val)) == ((1<<10)-1):
            return 1
        else:
            return 0

    if dp[pos][val][state] != -1:
        return dp[pos][val][state]

    ans = get_number(pos-1, val-1, state|(1<<val), dp) + get_number(pos-1, val+1, state|(1<<val), dp)
    dp[pos][val][state] = ans
    return ans


def solution(n: int):
    dp = [[[-1 for _ in range(1<<11)] for _ in range(11)] for _ in range(110)]
    ans = 0
    for i in range(1, 10):
        ans += get_number(n, i, 0, dp)
    return ans


def main():
    n = read_single_int()
    print(solution(n)%DIV)


if __name__ == '__main__':
    main()