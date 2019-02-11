# Title: 탈출
# Link: https://www.acmicpc.net/problem/16397

import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, max_time: int, g: int):
    if n == g:
        return 0

    numbers = [-1 for _ in range(100000)]
    queue = deque()
    queue.append((n, 0))

    while queue:
        num, t = queue.popleft()

        if t > max_time:
            return 'ANG'

        a = num+1
        if a <= 99999 and numbers[a] == -1:
            numbers[a] = t+1
            queue.append((a, t+1))
        
        if num == 0:
            b = 0
        elif num*2 >= 99999:
            b = 999999
        else:
            str_num = str(num*2)
            first = str(int(str_num[0])-1)
            b = int(first + str_num[1:])

        if b <= 99999 and numbers[b] == -1:
            numbers[b] = t+1
            queue.append((b, t+1))
        
        if numbers[g] != -1 and numbers[g] <= max_time:
            return numbers[g]

    return 'ANG'


def main():
    n, t, g = read_list_int()
    print(solution(n, t, g))


if __name__ == '__main__':
    main()