# Title: GCD(n, k) = 1
# Link: https://www.acmicpc.net/problem/11689:
# Link: https://www.acmicpc.net/problem/13926:

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def f1(x, n): return ((x*x) + 1) % n


def f2(x, n): return ((x*x) + 2) % n


def f3(x, n): return ((x*x) + 3) % n


def rho(n, f):
    x = 2
    y = 2
    d = 1
    count = 0
    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        d = gcd(abs(x - y), n)
        count += 1
        if count > 100000:
            return False
    if d == n:
        return False
    return d


def get_factoring(n, s, f_dic):
    # print('get_factoring {}'.format(n))
    f_dic[n] = True

    f = rho(n, f1)

    if n == 4 or n == 8 or n == 16:
        s.add(2)
        return
    elif n == 25 or n == 125:
        s.add(5)
        return
    elif n == 9 or n == 27 or n == 81:
        s.add(3)
        return

    if not f:
        f_2 = rho(n, f2)
        f_3 = rho(n, f3)
        if f_2 == f_3 == f and n != 4 and n != 8:
            s.add(n)
        else:
            if f_2:
                a, b = n//f_2, f_2
                if a not in f_dic:
                    get_factoring(a, s, f_dic)
                if b not in f_dic:
                    get_factoring(b, s, f_dic)
            if f_3:
                a, b = n//f_3, f_3
                if a not in f_dic:
                    get_factoring(a, s, f_dic)
                if b not in f_dic:
                    get_factoring(b, s, f_dic)
    else:
        if f:
            a, b = n//f, f
            if a not in f_dic:
                get_factoring(a, s, f_dic)
            if b not in f_dic:
                get_factoring(b, s, f_dic)


def num_gcd(n):
    if n == 1:
        return 1
    factors = set()
    f_dic = {}
    get_factoring(n, factors, f_dic)
    # print(factors)
    up, down = 1, 1
    for f in factors:
        up *= (f-1)
        down *= f
    return n * up // down


def sol(n):
    r = n
    for p in range(2, int(n**0.5)+1):
        if n % p == 0:
            while n % p == 0:
                n = n // p
            r = r - r//p
    if n > 1:
        r = r - r//n
    return r


if __name__ == '__main__':
    n = read_single_int()
    print(num_gcd(n))

    # for n in range(1000000000000000000, 0, -1):
    #     print('{} : {}'.format(n, num_gcd(n)))

    # print(num_gcd(999999999999999994))

    # print(rho(1546412477693, f1))
    # print(rho(1546412477693, f2))
    # print(rho(1546412477693, f3))
