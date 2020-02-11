# Title: 내가 살께, 아내 내가 살께
# Link: https://www.acmicpc.net/problem/18229

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, k: int, hands: list):
    for t in range(m):
        for p in range(n):
            hands[p][t+1] = hands[p][t+1] + hands[p][t]
            if hands[p][t+1] >= k:
                return f'{p+1} {t+1}'
            

def main():
    n, m, k = read_list_int()
    hands = []
    for _ in range(n):
        hands.append([0]+read_list_int())
    print(solution(n, m, k, hands))


if __name__ == '__main__':
    main()