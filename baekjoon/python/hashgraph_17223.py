# Title: 해시그래프
# Link: https://www.acmicpc.net/problem/17223

import sys
import copy


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, events: list, wnat: list):
    users = [[[i]] for i in range(n)]
    for f, t in events:
        last_from = copy.deepcopy(users[f][-1])
        last_from.append(t)
        users[t].append(last_from)
    
    for user in users:
        print(user)


def main():
    n, m = read_list_int()
    events = []
    for _ in range(m):
        events.append(read_list_int())
    want = read_list_int()
    print(solution(n, m, events, want))


if __name__ == '__main__':
    
    main()