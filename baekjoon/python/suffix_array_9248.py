# Title: Suffix Array
# Link: https://www.acmicpc.net/problem/9248

import sys


sys.setrecursionlimit(10 ** 6)


read_single_str = lambda: sys.stdin.readline().strip()


def get_suffix_array(s: str):
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


def get_lcp_array(sfx: list, s: str):
    n = len(s)
    lcp = [0 for _ in range(n)]
    prevsfx = [0 for _ in range(n+1)]
    plcp = [0 for _ in range(n+1)]

    prevsfx[sfx[0]] = -1
    for i in range(1, n):
        prevsfx[sfx[i]] = sfx[i-1]
    for i in range(n):
        common = 0
        if prevsfx[i]==-1:
            plcp[i] = 0
        else:
            while i+common < n and prevsfx[i]+common< n and s[i+common] == s[prevsfx[i]+common]:
                common += 1
            plcp[i] = common
            common = max(common-1, 0)
    for i in range(n):
        lcp[i] = plcp[sfx[i]]

    return lcp


def get_lcp_array_slow(suffix_array: list, s: str):
    lcp = ['x']
    first_index = suffix_array[0]
    for second_index in suffix_array[1:]:
        count = 0
        offset = 0
        while first_index+offset <= len(S) and second_index+offset <= len(S):
            if s[first_index-1+offset] != s[second_index-1+offset]:
                break
            count += 1
            offset += 1
        lcp.append(count)
        first_index = second_index

    return lcp



if __name__ == '__main__':
    S = read_single_str()
    suffix_array = get_suffix_array(S)
    print(' '.join(map(str, map(lambda x:x+1, suffix_array))))
    print(' '.join(map(str, get_lcp_array_slow(list(map(lambda x:x+1, suffix_array)), S))))
    # print('x ' + ' '.join(map(str, get_lcp_array(suffix_array, S)[1:])))
