# Title: Messi An-Gimossi
# Link: https://www.acmicpc.net/problem/17355

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

MOD = 1000000007


def gcd(a: int, b: int):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def solution(ps: list):
    pu = 1
    pd = 1
    for a, b in ps:
        pu = (((b-a)) * pu)
        pd = ((b) * pd)
    
    d = gcd(pu, pd)

    return '{} {}'.format((pu//d)%MOD, (pd//d)%MOD)


def main():
    n = read_single_int()
    ps = []
    for _ in range(n):
        ps.append(read_list_int())
    print(solution(ps))


if __name__ == '__main__':
    main()