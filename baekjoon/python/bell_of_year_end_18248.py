# Title: 제야의 종
# Link: https://www.acmicpc.net/problem/18248

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, sees: list):
    persons = [9999 for _ in range(n)]
    for c in range(m):
        see = []
        for p in range(n):
            see.append((p, sees[p][c]))
        can, cannot = [], []
        can_p = []
        for p, cansee in see:
            if cansee == 1:
                can.append(persons[p])
                can_p.append(p)
            else:
                cannot.append(persons[p])
        if can and cannot and max(can) > min(cannot):
            return 'NO'
        for p in can_p:
            persons[p] -= 1
    return 'YES'


def main():
    n, m = read_list_int()
    sees = []
    for _ in range(n):
        sees.append(read_list_int())
    print(solution(n, m, sees))


if __name__ == '__main__':
    main()