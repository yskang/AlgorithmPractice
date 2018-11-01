# Title: 카드 게임
# Link: https://www.acmicpc.net/problem/11062

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def maximum_score(turn: bool, left: int, right: int, cards: list, dp: list):
    if dp[0 if turn else 1][left][right] != -1:
        return dp[0 if turn else 1][left][right]
    
    if left > right:
        return 0    

    score = 0
    if turn:
        score = max(maximum_score(False, left+1, right, cards, dp) + cards[left],
                    maximum_score(False, left, right-1, cards, dp) + cards[right])
    else:
        score = min(maximum_score(True, left+1, right, cards, dp), 
                    maximum_score(True, left, right-1, cards, dp))
    dp[0 if turn else 1][left][right] = score
    return score


def solution(n: int, cards: list):
    dp = [[[-1 for _ in range(n+1)] for _ in range(n+1)] for _ in range(2)]
    return maximum_score(True, 0, n-1, cards, dp)


def main():
    t = read_single_int()
    for _ in range(t):
        n = read_single_int()
        cards = read_list_int()
        print(solution(n, cards))


if __name__ == '__main__':
    main()