# Title: 해시그래프
# Link: https://www.acmicpc.net/problem/17223

import sys
import random

sys.setrecursionlimit(10 ** 6)


def safe_int(s: str):
    return int(s.strip())

read_list_int = lambda: list(map(safe_int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, events: list, want: list):
    users = [[(i, 0)] for i in range(n)]
    for f, t in events:
        users[t].append((f, len(users[f])-1))

    a, a_event, b, b_event = want

    prev_user, prev_event = a, a_event

    while True:
        next_user, next_event = users[prev_user][prev_event]
        if (next_user, next_event) == (b, b_event):
            return 1
        if (next_user, next_event) == (prev_user, prev_event):
            return 0
        prev_user, prev_event = next_user, next_event

    return 0


def main():
    n, m = read_list_int()
    events = []
    for _ in range(m):
        events.append(read_list_int())
    want = read_list_int()
    print(solution(n, m, events, want))


def test():
    while True:
        n = random.randint(2, 100)
        m = random.randint(1, 10000)
        events = []
        users = [[0] for _ in range(n)]
        for _ in range(m):
            f = random.randint(0, n-1)
            t = random.randint(0, n-1)
            users[t].append(0)
            events.append([f, t])
        a = random.randint(0, n-1)
        a_event = random.randint(0, len(users[a])-1)
        b = random.randint(0, n-1)
        b_event = random.randint(0, len(users[b])-1)
        want = [a, a_event, b, b_event]

        print(n, m, want)
        print(solution(n, m, events, want))


if __name__ == '__main__':
    main()
    # test()