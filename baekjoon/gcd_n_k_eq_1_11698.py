# Title: GCD(n, k) = 1
# Link: https://www.acmicpc.net/problem/11698:
import math
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


def f1(x, n): return ((x*x) + 1)%n


def f2(x, n): return ((x*x) + 2)%n


def f3(x, n): return ((x*x) + 3)%n


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
    if d == n:
        return False
    return d


def get_factoring(n, s, f_dic):
    if n in f_dic:
        return
    f_dic[n] = True

    f = rho(n, f1)

    if n == 4 or n == 8 or n == 16:
        s.add(2)
        return

    if not f:
        f_2 = rho(n, f2)
        f_3 = rho(n, f3)
        if f_2 == f_3 and f_2 == False and n!=4 and n !=8:
            s.add(n)
        else:
            if f_2:
                get_factoring(n//f_2, s, f_dic)
                get_factoring(f_2, s, f_dic)
            if f_3:
                get_factoring(n//f_3, s, f_dic)
                get_factoring(f_3, s, f_dic)
    else:
        if f:
            get_factoring(n//f, s, f_dic)
            get_factoring(f, s, f_dic)



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


if __name__ == '__main__':
    # n = read_single_int()
    # print(num_gcd(n))
    for i in range(1000000000000, 0, -1):
        print('{}, {}'.format(i, num_gcd(i)))