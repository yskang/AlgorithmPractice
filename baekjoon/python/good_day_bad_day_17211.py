# Title: 좋은 날 싫은 날
# Link: https://www.acmicpc.net/problem/17211

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_words = lambda: sys.stdin.readline().strip().split(' ')

def my_round(n: float):
    if int(n) % 2 == 0:
        int_part = int(n)
        if n - int_part >= 0.5:
            return int_part+1
    return round(n)

def solution(n: int, mood: int, ps: list):
    dp = [[0, 0] for _ in range(n)]
    if mood == 0:
        dp[0] = [ps[0], ps[1]]
    else:
        dp[0] = [ps[2], ps[3]]
    
    for i in range(1, n):
        dp[i][0] = (ps[0] * dp[i-1][0]) + (ps[2] * dp[i-1][1])
        dp[i][1] = (ps[3] * dp[i-1][1]) + (ps[1] * dp[i-1][0])
    
    ans = [str(my_round(dp[n-1][0] * 1000)), str(my_round(dp[n-1][1] * 1000))]
    return '\n'.join(ans)


def main():
    n, mood = read_list_int()
    ps = read_list_words()
    ps = list(map(float, ps))
    print(solution(n, mood, ps))


if __name__ == '__main__':
    main()