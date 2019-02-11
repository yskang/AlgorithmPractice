# Title: 숨바꼭질
# Link: https://www.acmicpc.net/problem/1697

import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, k: int):
    if n == k:
        return 0
    numbers = defaultdict(lambda: -1)
    queue = deque()
    queue.append((n, 0))
    while True:
        (v, t) = queue.popleft()
        
        if numbers[v-1] == -1 and v-1 >= 0:
            numbers[v-1] = t+1
            queue.append((v-1, t+1))
        
        if numbers[v+1] == -1 and v+1 <= 100000:
            numbers[v+1] = t+1
            queue.append((v+1, t+1))
        
        if numbers[v*2] == -1 and v*2 <= 100000:
            numbers[v*2] = t+1
            queue.append((v*2, t+1))
        
        if numbers[k] != -1:
            return numbers[k]


def main():
    n, k = read_list_int()
    print(solution(n, k))


if __name__ == '__main__':
    main()