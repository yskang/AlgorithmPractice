# Title: 최솟값 찾기
# Link: https://www.acmicpc.net/problem/11003

import sys
import collections


read_list_int = lambda: sys.stdin.readline().strip().split(' ')


def solution(list_length: int, window_width: int, numbers: list):
    window = collections.deque([])
    for i, number in enumerate(numbers):
        num = int(number)
        while len(window) != 0 and window[0][1] < i-window_width+1:
            window.popleft()
        while len(window) != 0 and num <= window[-1][0]:
            window.pop()
        window.append((num, i))
        print(window[0][0], end=' ')


def main():
    n, l = read_list_int()
    n, l = int(n), int(l)
    a = read_list_int()
    solution(int(n), int(l), a)


if __name__ == '__main__':
    main()