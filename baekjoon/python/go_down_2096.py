# Title: 내려가기
# Link: https://www.acmicpc.net/problem/2096

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, block: list):
    old_score = [0, 0, 0]
    new_score = [0, 0, 0]
    min_num, max_num = 0, 0

    for i, score in enumerate(block[0]):
        old_score[i] = score

    for i in range(1, n):
        new_score[0] = max(old_score[0], old_score[1]) + block[i][0]
        new_score[1] = max(old_score[0], old_score[1], old_score[2]) + block[i][1]
        new_score[2] = max(old_score[1], old_score[2]) + block[i][2]
        new_score, old_score = old_score, new_score
    max_num = max(old_score)

    for i, score in enumerate(block[0]):
        old_score[i] = score

    for i in range(1, n):
        new_score[0] = min(old_score[0], old_score[1]) + block[i][0]
        new_score[1] = min(old_score[0], old_score[1], old_score[2]) + block[i][1]
        new_score[2] = min(old_score[1], old_score[2]) + block[i][2]
        new_score, old_score = old_score, new_score
    min_num = min(old_score)

    return'{} {}'.format(max_num, min_num)


def main():
    n = read_single_int()
    block = []
    for _ in range(n):
        block.append(read_list_int())
    print(solution(n, block))


if __name__ == '__main__':
    main()