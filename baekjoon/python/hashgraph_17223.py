# Title: 해시그래프
# Link: https://www.acmicpc.net/problem/17223

import sys
import random

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().replace('\r', '').replace('\n', '').strip().split(' ')))

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
    n, m = read_list_int()
    transmit = []
    for _ in range(m):
        transmit.append(read_list_int())
    want = read_list_int()
    print(solution(n, m, transmit, want))


if __name__ == '__main__':
    main()
    # test()