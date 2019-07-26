# Title: 나머지
# Link: https://www.acmicpc.net/problem/3052

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(ns: list):
    r = set()
    for n in ns:
        r.add(n%42)
    return len(r)
    

def main():
    ns = []
    for _ in range(10):
        ns.append(read_single_int())
    print(solution(ns))


if __name__ == '__main__':
    main()