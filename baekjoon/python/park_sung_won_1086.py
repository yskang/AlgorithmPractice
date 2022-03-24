# Title: 박성원
# Link: https://www.acmicpc.net/problem/1086

import sys
from math import factorial


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def get_count(used: int, acc: int, dp: list, n: int, ns: int, tens_mod_k: list, ns_mod_k: list, lens: list, k: int):
    if dp[used][acc] != -1:
        return dp[used][acc]
    if used+1 == 1<<n:
        dp[used][acc] = 1 if acc == 0 else 0
        return dp[used][acc]

    res = 0
    for i in range(n):
        if (1 << i) & used == 0:
            res += get_count(used|(1<<i), (acc*tens_mod_k[lens[i]]+ns_mod_k[i])%k, dp, n, ns, tens_mod_k, ns_mod_k, lens, k)
    dp[used][acc] = res
    return res


def solution(n: int, ns: list, k: int):
    lens = [len(str(x)) for x in ns]
    tens_mod_k = [pow(10, i)%k for i in range(sum(lens)+1)]
    ns_mod_k = [i%k for i in ns]
    dp = [[-1 for _ in range(k)] for _ in range(1<<n)]
    count = get_count(0, 0, dp, n, ns, tens_mod_k, ns_mod_k, lens, k)
    total = factorial(n)
    common_divider = gcd(count, total)
    return '{}/{}'.format(count//common_divider, total//common_divider)


def main():
    n = read_single_int()
    ns = []
    for _ in range(n):
        ns.append(read_single_int())
    k = read_single_int()
    print(solution(n, ns, k))


if __name__ == '__main__':
    main()