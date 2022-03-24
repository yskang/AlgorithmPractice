# Title: 세훈이의 선물가게
# Link: https://www.acmicpc.net/problem/17225

import sys
from collections import deque, defaultdict


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_words = lambda: sys.stdin.readline().strip().split()


def solution(a: int, b: int, n: int, orders: list):
    sangmin = []
    sangmin_last = -1
    jisoo = []
    jisoo_last = -1
    idx = []
    for time, color, count in orders:
        if color == 'B':
            if sangmin_last < time:
                for i in range(count):
                    sangmin.append(time+a*(i))
                sangmin_last = sangmin[-1]+a
            else:
                base = sangmin_last
                for i in range(count):
                    sangmin.append(base+a*(i))
                sangmin_last = sangmin[-1]+a
        else:
            if jisoo_last < time:
                for i in range(count):
                    jisoo.append(time+b*(i))
                jisoo_last = jisoo[-1]+b
            else:
                base = jisoo_last
                for i in range(count):
                    jisoo.append(base+b*(i))
                jisoo_last = jisoo[-1]+b

    # print(sangmin)
    # print(jisoo)

    sangmin = deque(sangmin)
    jisoo = deque(jisoo)
    
    number = 1
    sangmin_g = []
    jisoo_g = []
    while True:
        if sangmin and jisoo:
            if sangmin[0] <= jisoo[0]:
                sangmin_g.append(number)
                number += 1
                sangmin.popleft()
            elif sangmin[0] >= jisoo[0]:
                jisoo_g.append(number)
                number += 1
                jisoo.popleft()
            # else:
            #     sangmin_g.append(number)
            #     number += 1
            #     jisoo_g.append(number)
            #     number += 1
            #     sangmin.popleft()
            #     jisoo.popleft()
        elif not sangmin and jisoo:
            jisoo_g.append(number)
            number += 1
            jisoo.popleft()
        elif not jisoo and sangmin:
            sangmin_g.append(number)
            number += 1
            sangmin.popleft()
        elif not sangmin and not jisoo:
            break

    print(len(sangmin_g))
    print(' '.join(map(str, sangmin_g)))
    print(len(jisoo_g))
    print(' '.join(map(str, jisoo_g)))           



def main():
    a, b, n = read_list_int()
    orders = []
    for _ in range(n):
        t, c, m = read_list_words()
        orders.append([int(t), c, int(m)])
    solution(a, b, n, orders)


if __name__ == '__main__':
    main()
