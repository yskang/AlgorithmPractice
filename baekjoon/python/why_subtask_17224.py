# Title: APC는 왜 서브태스크 대회가 되었을까?
# Link: https://www.acmicpc.net/problem/17224

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, l: int, k: int, problems: list):
    scores = []
    for easy, hard in problems:
        if hard <= l:
            scores.append(140)
        elif easy <= l:
            scores.append(100)
        else:
            scores.append(0)
    scores = sorted(scores, reverse=True)
    return sum(scores[:k])



def main():
    n, l, k = read_list_int()
    problems = []
    for _ in range(n):
        problems.append(read_list_int())
    print(solution(n, l, k, problems))


if __name__ == '__main__':
    main()