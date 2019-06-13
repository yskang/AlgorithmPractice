# Title: 해시그래프
# Link: https://www.acmicpc.net/problem/17223

import sys
import random
import operator
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

<<<<<<< HEAD
XRAW = sys.stdin.read().split()
XIN = iter(XRAW)
read_one_number = lambda: int(next(XIN))
=======
XRAW = __import__('sys').stdin.read().split()
XIN = iter(XRAW)
read_one_number = lambda: int(next(XIN))

>>>>>>> 1a98d51dfbff78c92f2d6f98533885e010f8252e


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
<<<<<<< HEAD
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
=======
    n = read_one_number()
    m = read_one_number()
    transmit = []
    for _ in range(m):
        send = read_one_number()
        receive = read_one_number()
        transmit.append([send, receive])
    want = (read_one_number(), read_one_number(), read_one_number(), read_one_number())
    print(solution(n, m, transmit, want))
>>>>>>> 1a98d51dfbff78c92f2d6f98533885e010f8252e


if __name__ == '__main__':
    main()
