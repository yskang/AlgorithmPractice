# Title: 러버덕을 사랑하는 모임
# Link: https://www.acmicpc.net/problem/18233

import sys
from itertools import combinations
from functools import reduce


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def solution(n: int, p: int, e: int, reqs: list):
    for req in list(combinations(reqs, p)):
        _, small, big = reduce(lambda x, y: (0, x[1]+y[1], x[2]+y[2]), req, (0, 0, 0))
        if small <= e <= big:
            diff = e - small
            res = [0 for _ in range(n)]
            for i, s, b in req:
                res[i] = s
            if diff == 0:
                return ' '.join(map(str, res))

            for i, s, b in req:
                if b-s < diff:
                    diff -= (b-s)
                    res[i] = b
                elif b-s == diff:
                    res[i] = b
                    return ' '.join(map(str, res))
                else:
                    res[i] += diff
                    return ' '.join(map(str, res))
    return -1


def main():
    n, p, e = read_list_int()
    reqs = []
    for i in range(n):
        reqs.append([i] + read_list_int())
    print(solution(n, p, e, reqs))


if __name__ == '__main__':
    main()