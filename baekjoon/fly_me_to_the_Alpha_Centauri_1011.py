# https://www.acmicpc.net/problem/1011
import sys


def count_of_warp(points):
    distance = points[1] - points[0]
    warp_count = 0
    warp_dist = 1

    while distance > warp_dist:
        warp_count += 1
        distance = distance - 2*warp_dist
        if distance < 0:
            distance = distance + 2*warp_dist
            warp_dist -= 1
            warp_count -= 1
            break
        warp_dist += 1

    if distance == 0:
        return warp_count * 2
    elif distance > warp_dist:
        return warp_count * 2 + 2
    return warp_count * 2 + 1


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        print(count_of_warp(list(map(int, sys.stdin.readline().strip().split()))))

