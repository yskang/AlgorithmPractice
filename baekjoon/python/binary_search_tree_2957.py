# Title: 이진 탐색 트리
# Link: https://www.acmicpc.net/problem/2957

import sys
import bisect
import random
from collections import deque as dq
from collections import defaultdict as dd


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def main():
    ret = []
    MXN = 300000
    n = read_single_int()
    a = [0 for _ in range(n+1)]
    l = [0 for _ in range(n+2)]
    r = [0 for _ in range(n+2)]
    lev = [0 for _ in range(n+2)]
    res = 0

    for i in range(1, n+1):
        a[i] = read_single_int()
        l[i] = i-1
        r[i] = i+1
    for i in range(n, 0, -1):
        r[l[a[i]]] = r[a[i]]
        l[r[a[i]]] = l[a[i]]
    
    lev[0] = lev[n+1] = -1
    for i in range(1, n+1):
        lev[a[i]] = max(lev[l[a[i]]], lev[r[a[i]]]) + 1
        res += lev[a[i]]
        ret.append(str(res))
    print('\n'.join(ret))


if __name__ == '__main__':
    main()