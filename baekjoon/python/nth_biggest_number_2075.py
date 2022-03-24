# Title: N번째 큰 수
# Link: https://www.acmicpc.net/problem/2075

import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def main():
    n = read_single_int()
    nums = []
    if n == 1:
        print(read_list_int()[0])
        return

    for v in read_list_int():
        heappush(nums, v)

    for _ in range(n-1):
        for v in read_list_int():
            heappush(nums, v)
        for _ in range(n):
            heappop(nums)
    
    print(heappop(nums))


if __name__ == '__main__':
    main()