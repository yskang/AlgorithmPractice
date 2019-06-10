# Title: 해시그래프
# Link: https://www.acmicpc.net/problem/17223

import sys
import random

sys.setrecursionlimit(10 ** 6)

XRAW = __import__('sys').stdin.read().split()
XIN = iter(XRAW)
read_one_number = lambda: int(next(XIN))


def solution(n: int, m: int, transmit: list, want: list):
    events = [[(i, 0)] for i in range(n)]
    for send, receive in transmit:
        events[receive].append((send, len(events[send])-1))

    prev_user, prev_event, target_user, target_event = want

    while True:
        next_user, next_event = events[prev_user][prev_event]
        if (next_user, next_event) == (target_user, target_event):
            return 1
        if (next_user, next_event) == (prev_user, prev_event):
            return 0
        prev_user, prev_event = next_user, next_event

    return 0


def main():
    n = read_one_number()
    m = read_one_number()
    transmit = []
    for _ in range(m):
        send = read_one_number()
        receive = read_one_number()
        transmit.append([send, receive])
    want = (read_one_number(), read_one_number(), read_one_number(), read_one_number())
    print(solution(n, m, transmit, want))


if __name__ == '__main__':
    main()
