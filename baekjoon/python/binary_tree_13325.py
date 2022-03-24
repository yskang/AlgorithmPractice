# Title: 이진 틀;
# Link: https://www.acmicpc.net/problem/13325

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(k: int, ns: list):
    s = 0
    ps = [(0, 2)]
    for i in range(1, k):
        s += 2**i
        ps.append((s, 2**(i+1)))


    total = 0

    prevs = [0] * 2**k
    for p in reversed(ps):

        for i in range(p[0], p[0]+p[1]):
            total += ns[i]
            ns[i] += prevs[i-p[0]]


        prevs = []
        for i in range(p[0], p[0]+p[1], 2):
            prevs.append(max(ns[i], ns[i+1]))
            total += abs(ns[i] - ns[i+1])
    
    return total


def main():
    k = read_single_int()
    ns = read_list_int()
    print(solution(k, ns))


if __name__ == '__main__':
    main()