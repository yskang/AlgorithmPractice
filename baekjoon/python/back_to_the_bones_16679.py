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
    temp_total = total
    sum_poped = 0
    poped = []

    while ns:
        value, pos = ns.pop()
        poped.append(pos)
        sum_poped += value
        temp_total -= value
        temp_total += 6

        if temp_total >= k:
            t = len(poped)
            remains = total - sum_poped

            p = 1
            m, mm = divmod(k - remains, t)
            for _ in range(t-mm):
                p *= (7-m)
            for _ in range(mm):
                p *= (7-(m+1))

            a = p*pow(6, n-t)
            b = [1 if i in poped else 0 for i in range(n)]
            ans_map[a] = b
            print(a, b)
    max_p = max(ans_map.keys())

    return max_p, ans_map[max_p]


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