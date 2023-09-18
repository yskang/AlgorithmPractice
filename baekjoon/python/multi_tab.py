# Title: 멀티탭 스케쥴링
# Link: https://www.acmicpc.net/problem/tab

import sys


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, k: int, electronics: list) -> int:
    count = 0
    plugs = set()

    while electronics:
        device = electronics.pop(0)
        # if device in plugs, continue
        if device in plugs:
            continue
        # if plugs has empty slot, plug device
        if len(plugs) < n:
            plugs.add(device)
            continue
        # if not, unplug device, which one?
        # choose the device that will be used last
        copyed_plugs = set(plugs)
        for unplugged in electronics:
            if len(copyed_plugs) == 1:
                break
            if unplugged in copyed_plugs:
                copyed_plugs.remove(unplugged)
        
        plugs.remove(copyed_plugs.pop())
        count += 1
        plugs.add(device)

    return count


def main():
    n, k = read_list_int()
    electronics = read_list_int()
    print(solution(n, k, electronics))


if __name__ == '__main__':
    main()