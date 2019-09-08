# Title: 숨바꼭질 4
# Link: https://www.acmicpc.net/problem/13913

import sys
from heapq import heappop, heappush
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)
INF = 10**10


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def dijkstra(n: int, k: int):
    distances = defaultdict(lambda: INF)
    paths = defaultdict(lambda: None)
    hq = []
    distances[n] =  0
    heappush(hq, (0, n))

    while hq:
        dist, p = heappop(hq)
        if distances[p] < dist:
            continue
        
        if p-1 > -1:
            if dist + 1 < distances[p-1]:
                distances[p-1] = dist+1
                heappush(hq, (dist+1, p-1))
                paths[p-1] = p

        if p+1 < 100001:
            if dist + 1 < distances[p+1]:
                distances[p+1] = dist+1
                heappush(hq, (dist+1, p+1))
                paths[p+1] = p

        if p*2 < 100001:
            if dist + 1 < distances[p*2]:
                distances[p*2] = dist+1
                heappush(hq, (dist+1, p*2))
                paths[p*2] = p
        
        if paths[k]:
            break
    
    return paths


def solution(n: int, k: int):
    if n == k :
        print(0)
        print(n)
        return
        
    paths = dijkstra(n, k)
    ans = [k]
    while True:
        ans.append(paths[ans[-1]])
        if ans[-1] == n:
            break
    print(len(ans)-1)
    print(*reversed(ans))


def main():
    n, k = read_list_int()
    solution(n, k)


if __name__ == '__main__':
    main()