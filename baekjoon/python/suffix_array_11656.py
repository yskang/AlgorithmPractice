# Title: 접미사 배열
# Link: https://www.acmicpc.net/problem/11656

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()

def solution(s: str):
    n = len(s)
    lim = max(257, n+1)
    sfx = [i for i in range(0, n)]
    g = [ord(s[i]) for i in range(n)] + [0 for _ in range(n)]
    ng = [0 for _ in range(n)] + [0 for _ in range(n)]
    order_to_idx = [0 for _ in range(n+1)]
    cnt = []
    tmp = g
    t = 1
    while t < n:
        cnt = [0 for _ in range(lim)]
        for i in range(n):
            cnt[g[min(i+t, n)]] += 1
        for i in range(1, lim):
            cnt[i] += cnt[i-1]
        for idx in range(n-1, -1, -1):
            cnt[g[min(idx+t, n)]] -= 1
            order_to_idx[cnt[g[min(idx+t, n)]]] = idx

        cnt = [0 for _ in range(lim)]
        for i in range(n):
            cnt[g[i]] += 1
        for i in range(1, lim):
            cnt[i] += cnt[i-1]
        for i in range(n-1, -1, -1):
            cnt[g[order_to_idx[i]]] -= 1
            sfx[cnt[g[order_to_idx[i]]]] = order_to_idx[i]

        # cmp = lambda i, j: g[i+t]<g[j+t] if g[i]==g[j] else g[i] < g[j]
        ng[sfx[0]] = 1
        for i in range(1, n):
            # if cmp(sfx[i-1], sfx[i]):
            if g[sfx[i-1]] == g[sfx[i]]:
                if g[sfx[i-1]+t] < g[sfx[i]+t]:
                    ng[sfx[i]] = ng[sfx[i-1]]+1
                else:
                    ng[sfx[i]] = ng[sfx[i-1]]
            else:
                if g[sfx[i-1]] < g[sfx[i]]:
                    ng[sfx[i]] = ng[sfx[i-1]]+1
                else:
                    ng[sfx[i]] = ng[sfx[i-1]]                    

        tmp = g
        g = ng
        ng = tmp
        t <<= 1
    return sfx


def main():
    s = read_single_str()
    for sf in solution(s):
        print(s[sf:])


if __name__ == '__main__':
    main()