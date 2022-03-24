# Title: 게임 개발
# Link: https://www.acmicpc.net/problem/1516
import copy
import sys

import heapq

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def minimum_time_to_build_all_building(buildings, times, in_degrees, N):
    hq = []
    pluses = [[] for _ in range(N+1)]

    for num in range(1, N+1):
        if in_degrees[num] == 0:
            heapq.heappush(hq, num)

    while len(hq) > 0:
        popped = heapq.heappop(hq)
        for next_building in buildings[popped]:
            pluses[next_building].append(times[popped])
            in_degrees[next_building] -= 1
            if in_degrees[next_building] == 0:
                heapq.heappush(hq, next_building)
                times[next_building] += max(pluses[next_building])

    return '\n'.join(map(str, times[1:]))


if __name__ == '__main__':
    N = read_single_int()
    times = [0 for _ in range(N+1)]
    buildings = [[] for _ in range(N+1)]
    in_degrees = [0 for _ in range(N+1)]
    for n in range(1, N+1):
        line = read_list_int()
        in_degrees[n] = len(line)-2
        times[n] = line[0]
        for m in line[1:-1]:
            buildings[m].append(n)

    print(minimum_time_to_build_all_building(buildings, times, in_degrees, N))