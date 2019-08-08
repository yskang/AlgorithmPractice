# Title: 공유기 설치
# Link: https://www.acmicpc.net/problem/2110

import sys

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, ns: list, c: int):
    ns = sorted(ns)
    left, right = 1, ns[-1]-ns[0]
    ans = -1

    while left <= right:
        mid = (left+right)//2
        installed = 1
        last = ns[0]
        for house in ns[1:]:
            if house-last >= mid:
                installed += 1
                last = house
        
        if installed >= c:
            left = mid+1
            ans = mid
        else:
            right = mid-1
    
    return ans


def main():
    n, c = read_list_int()
    ns = []
    for _ in range(n):
        ns.append(read_single_int())
    print(solution(n, ns, c))


if __name__ == '__main__':
    main()