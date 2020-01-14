# Title: 큐 2
# Link: https://www.acmicpc.net/problem/18258

import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)


read_list_words = lambda: sys.stdin.readline().strip().split(' ')
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(q: deque, command: list):
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)


def main():
    n = read_single_int()
    q = deque()
    for _ in range(n):
        solution(q, read_list_words())


if __name__ == '__main__':
    main()