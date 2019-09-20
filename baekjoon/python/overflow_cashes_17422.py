# Title: 지폐가 넘쳐흘러
# Link: https://www.acmicpc.net/problem/17422

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_max(n: int, ns: list, root: int, cache: list):
    if root > n:
        return 0
    if cache[root] != -1:
        return cache[root]
    res = ns[root] + max(get_max(n, ns, root*2, cache), get_max(n, ns, root*2+1, cache))
    cache[root] = res
    return res


def get(n: int, ns: list, q: int, cache: list, cache2: list):
    if cache2[q] != -1:
        return cache2[q]
    ans = ns[q] + get_max(n, ns, q*2, cache) + get_max(n, ns, q*2+1, cache)
    cache2[q] = ans
    return ans


def solution(n: int, ns: list, q: int, qs: list):
    max_val = -1
    cache = [-1 for _ in range(n+1)]
    cache2 = [-1 for _ in range(n+1)]
    to_find = False
    for num, val in qs:
        ns[num] = val

        k = num
        while True:
            if cache2[k] == max_val:
                to_find = True
            cache[k] = -1
            cache2[k] = -1
            if k == 1:
                break
            k //= 2

        if to_find:
            to_find = False
            max_val = 0
            for i in range(1, n+1):
                max_val = max(max_val, get(n, ns, i, cache, cache2))
        print(max_val)


def main():
    n = read_single_int()
    ns = [0] + read_list_int()
    q = read_single_int()
    qs = [[1, ns[1]]]
    for _ in range(q):
        qs.append(read_list_int())
    solution(n, ns, q, qs)


if __name__ == '__main__':
    main()