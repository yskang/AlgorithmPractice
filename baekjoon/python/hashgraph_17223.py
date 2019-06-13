# Title: 해시그래프
# Link: https://www.acmicpc.net/problem/17223

import sys
import random
import operator
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

XRAW = sys.stdin.read().split()
XIN = iter(XRAW)
read_one_number = lambda: int(next(XIN))


def dfs(node: int, g: defaultdict, visit: list):
    if visit[node]:
        return
    visit[node] = True

    for n in g[node]:
        dfs(n, g, visit)


def solution(n: int, m: int, g: defaultdict, want: list, last: int, users: list):
    visit = [False for _ in range(last+1)]
    user, event, target_user, target_event = want
    dfs(users[user][event], g, visit)
    return 1 if visit[users[target_user][target_event]] else 0


def main():
    g = defaultdict(lambda: [])
    n = read_one_number()
    m = read_one_number()

    users = [[] for _ in range(n)]
    for i in range(n):
        users[i].append(i)
    last = n-1
    for _ in range(m):
        sender = read_one_number()
        receiver = read_one_number()
        last += 1
        users[receiver].append(last)
        g[last].append(users[receiver][-2])
        g[last].append(users[sender][-1])

    want = (read_one_number(), read_one_number(), read_one_number(), read_one_number())
    print(solution(n, m, g, want, last, users))


if __name__ == '__main__':
    main()
