# Title: 피보나치 수와 최대 공약수
# Link: https://www.acmicpc.net/problem/11778:

import sys

sys.setrecursionlimit(10 ** 6)

def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def get_gcd_of_fibonacci(n, m):
    gcd_val = gcd(n, m)
    
    ans = [[1, 0], [1, 0]]
    a = [[1, 1], [1, 0]]

    while gcd_val > 0:
        if gcd_val % 2 == 1:
            ans = [[(ans[0][0]*a[0][0]+ans[0][1]*a[1][0]) % 1000000007, (ans[0][0]*a[0][1]+ans[0][1]*a[1][1]) % 1000000007],
            [(ans[1][0]*a[0][0]+ans[1][1]*a[1][0]) % 1000000007, (ans[1][0]*a[0][1]+ans[1][1]*a[1][1]) % 1000000007]]

        a = [[(a[0][0]*a[0][0]+a[0][1]*a[1][0]) % 1000000007, (a[0][0]*a[0][1]+a[0][1]*a[1][1]) % 1000000007],
            [(a[1][0]*a[0][0]+a[1][1]*a[1][0]) % 1000000007, (a[1][0]*a[0][1]+a[1][1]*a[1][1]) % 1000000007]]

        gcd_val //= 2

    return ans[0][1] % 1000000007


if __name__ == '__main__':
    n, m = read_list_int()
    print(get_gcd_of_fibonacci(n, m))
