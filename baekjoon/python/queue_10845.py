# Title: 큐
# Link: https://www.acmicpc.net/problem/10845

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_str = lambda: list(sys.stdin.readline().strip().split())


def solution(ops: list):
    q = deque()
    for op in ops:
        if op[0] == 'push':
            q.append(op[1])
        elif op[0] == 'pop':
            print(q.popleft() if q else -1)
        elif op[0] == 'size':
            print(len(q))
        elif op[0] == 'empty':
            print(0 if q else 1)
        elif op[0] == 'front':
            print(q[0] if q else -1)
        elif op[0] == 'back':
            print(q[-1] if q else -1)

def main():
    n = read_single_int()
    ops = []
    for _ in range(n):
        ops.append(read_list_str())
    solution(ops)


if __name__ == '__main__':
    main()