# Title: 가운데를 말해요
# Link: https://www.acmicpc.net/problem/1655

import sys
from heapq import heappush, heappop

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


INF = 9999999999


def solution(ns: list):
    lowers = []
    uppers = []
    center = INF
    heappush(lowers, INF)
    heappush(uppers, INF)
    ans = []
    for i, n in enumerate(ns, 1):
        if i % 2 == 1:
            if -lowers[0] < n < uppers[0]:
                center = n
            elif uppers[0] < n:
                heappush(uppers, n)
                center = heappop(uppers)
            else:
                heappush(lowers, -n)
                center = -heappop(lowers)
            ans.append(center)
        else:
            if center < n:
                heappush(lowers, -center)
                heappush(uppers, n)
            else:
                heappush(lowers, -n)
                heappush(uppers, center)
            ans.append(min(-lowers[0], uppers[0]))
            center = INF
    return '\n'.join(map(str, ans))


def main():
    n = read_single_int()
    ns = []
    for _ in range(n):
        ns.append(read_single_int())
    print(solution(ns))


if __name__ == '__main__':
    main()