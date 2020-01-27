# Title: 내 생각에 A번인 단순 dfs 문제가 이 대회에서 E번이 되어버린 건에 관하여(Easy)
# Link: https://www.acmicpc.net/problem/18251

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


INF = 10**10
MIN = -INF


def get_maximum_subarray(ns: list, d: int, u: int):
    res = MIN
    sub_sums = MIN
    for n in ns:
        if d <= n[1] <= u:
            sub_sum = max(sub_sums + n[0], n[0])
            res = max(res, sub_sum)
            sub_sums = sub_sum
    return res


def solution(n: int, ws: list):
    ns = [None for _ in range(n)]
    n += 1
    c = 0
    j = 0
    while n != 1:
        c += 1
        n = n//2
        i = -1
        while True:
            i += n
            if i < len(ns):
                if ns[i] == None:
                    ns[i] = (ws[j], c)
                    j += 1
                else:
                    continue
            else:
                break

    max_weight = MIN
    
    for d in range(1, c+1):
        for u in range(d, c+1):
            max_weight = max(get_maximum_subarray(ns, d, u), max_weight)

    return max_weight



def main():
    n = read_single_int()
    ws = read_list_int()
    print(solution(n, ws))


if __name__ == '__main__':
    main()