# Title: 국영수
# Link: https://www.acmicpc.net/problem/10825

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(scores: list):
    return sorted(scores, key=lambda x: (100-x[1], x[2], 100-x[3], x[0]))


def main():
    N = read_single_int()
    scores = []
    for _ in range(N):
        name, korean, english, maths = sys.stdin.readline().strip().split(' ')
        scores.append((name, int(korean), int(english), int(maths)))
    print('\n'.join(map(lambda x: x[0], solution(scores))))


if __name__ == '__main__':
    main()