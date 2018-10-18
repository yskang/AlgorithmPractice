# Title: 카드 구매하기
# Link: https://www.acmicpc.net/problem/11052

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(num_card: int, packs: list):
    d = [0 for _ in range(num_card+1)]

    for i in range(1, num_card+1):
        d[i] = max([d[i-j] + packs[j-1] for j in range(1, i+1)])
    
    return d[num_card]


def main():
    N = read_single_int()
    P = read_list_int()
    print(solution(N, P))


if __name__ == '__main__':
    main()