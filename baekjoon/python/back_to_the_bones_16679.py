# Title: Back to the bones
# Link: https://www.acmicpc.net/problem/16679

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, k: int, ns: list):
    total = sum(ns)
    if total >= k:
        return pow(6, n), [0 for _ in range(n)]

    ns = list(zip(ns, [i for i in range(len(ns))]))
    ns = sorted(ns, key=lambda x: x[0], reverse=True)

    ans_map = {}
    sum_poped = 0
    poped = []

    while ns:
        value, pos = ns.pop()
        poped.append(pos)
        sum_poped += value
        poped_len = len(poped)

        if total - sum_poped + 6*poped_len >= k:

            a = calc_probablity(poped_len, k - (total-sum_poped)) * pow(6, n-poped_len)
            b = [1 if i in poped else 0 for i in range(n)]
            ans_map[a] = b

    max_p = max(ans_map.keys())

    return max_p, ans_map[max_p]


def count_make(n: int, k: int, cache: list):
    # if n < 0 or k < 0:
    #     return 0
    if cache[k][n] != -1:
        return cache[k][n]

    if n == 1:
        if 1 <= k <= 6:
            cache[k][n] = 1
            return 1
        else:
            cache[k][n] = 0
            return 0

    s = 0
    for i in range(1, 7):
        s += count_make(n-1, k-i, cache)

    cache[k][n] = s    
    return s



def calc_probablity(n: int, k: int):
    cache = [[-1 for _ in range(n+1)] for _ in range(k*6+1)]
    s = 0
    for i in range(k, 6*n+1):
        t = count_make(n, i, cache)
        s += t
    return s


def main():
    t = read_single_int()
    for _ in range(t):
        n, k = read_list_int()
        ns = read_list_int()
        p, dices = solution(n, k, ns)
        print(p)
        print(' '.join(map(str, dices)))

if __name__ == '__main__':
    main()