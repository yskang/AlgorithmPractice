# Title: 수열 섞기
# Link: https://www.acmicpc.net/problem/16209

import sys
import collections
import bisect

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, e: list):
    dq_plus = collections.deque()
    dq_minus = collections.deque()
    e = sorted(e)

    z = bisect.bisect_left(e, 0)
    
    if (len(e) - z) % 2 == 0:
        d = True
    else:
        d = False

    for i in range(len(e)-1, z-1, -1):
        if d:
            dq_plus.append(e[i])
            d = not d
        else:
            dq_plus.appendleft(e[i])
            d = not d

    if z % 2 == 0:
        d = False
    else:
        d = True

    for i in range(0, z):
        if d:
            dq_minus.append(e[i])
            d = not d
        else:
            dq_minus.appendleft(e[i])
            d = not d

    return ' '.join(map(str, dq_minus)) + ' ' + ' '.join(map(str, dq_plus))


def main():
    n = read_single_int()
    e = read_list_int()
    print(solution(n, e))


if __name__ == '__main__':
    main()