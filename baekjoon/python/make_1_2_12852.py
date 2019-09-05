# Title: 1로 만들기 2
# Link: https://www.acmicpc.net/problem/12852

import sys
from collections import defaultdict
from heapq import heappop, heappush


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
INF = 10**10


def dijkstra(n):
    distances = defaultdict(lambda: INF)
    paths = defaultdict(lambda: None)
    pq = []
    heappush(pq, (0, n))

    while pq:
        dist, num = heappop(pq)

        if distances[num] < dist:
            continue
        
        if num % 3 == 0:
            if dist + 1 < distances[num//3]:
                distances[num//3] = dist+1
                heappush(pq, (dist+1, num//3))
                paths[num//3] = num
        if num % 2 == 0:
            if dist + 1 < distances[num//2]:
                distances[num//2] = dist+1
                heappush(pq, (dist+1, num//2))
                paths[num//2] = num
        if num-1 >= 0 and dist + 1 < distances[num-1]:
            distances[num-1] = dist+1
            heappush(pq, (dist+1, num-1))
            paths[num-1] = num
        
        if paths[1]:
            break

    return paths


def solution(n: int):
    if n == 1:
        print('0\n1')
        return
    paths = dijkstra(n)
    ans = [1]
    while True:
        ans.append(paths[ans[-1]])
        if ans[-1] == n:
            break
    print(len(ans)-1)
    print(*reversed(ans))


def main():
    n = read_single_int()
    solution(n)


if __name__ == '__main__':
    main()