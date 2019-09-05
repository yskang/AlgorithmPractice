# Title: 1로 만들기 2
# Link: https://www.acmicpc.net/problem/12852

import sys
from collections import deque
from copy import deepcopy


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    que = deque()
    que.append((n, []))
    while que:
        num, parents = que.popleft()
        if num == 1:
            print(len(parents))
            print(*parents, end='')
            print(' 1')
            break

        new_parents = deepcopy(parents)
        new_parents.append(num)

        if num % 2 == 0:
            que.append((num//2, deepcopy(new_parents)))
        if num % 3 == 0:
            que.append((num//3, deepcopy(new_parents)))
        que.append((num-1, deepcopy(new_parents)))


def main():
    n = read_single_int()
    solution(n)


if __name__ == '__main__':
    main()