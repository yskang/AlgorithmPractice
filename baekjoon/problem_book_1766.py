# Title: 문제집
# Link: https://www.acmicpc.net/problem/1766

import sys

import heapq

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_problem_order(problems, in_degrees, N):
    order = []
    hq = []
    for number in range(1, N+1):
        if in_degrees[number] == 0:
            heapq.heappush(hq, number)
    while hq:
        popped = heapq.heappop(hq)
        order.append(popped)
        for number in problems[popped]:
            in_degrees[number] -= 1
            if in_degrees[number] == 0:
                heapq.heappush(hq, number)
    return ' '.join(map(str, order))


if __name__ == '__main__':
    N, M = read_list_int()
    problems = [[] for _ in range(N+1)]
    in_degrees = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = read_list_int()
        problems[a].append(b)
        in_degrees[b] += 1
    print(get_problem_order(problems, in_degrees, N))