# Title: 링
# Link: https://www.acmicpc.net/problem/3036

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a


def calc_spins(rings):
    main_ring = rings[0]
    spins = []
    for ring in rings[1:]:
        divisor = gcd(main_ring, ring)
        spins.append('{}/{}'.format(main_ring//divisor, ring//divisor))

    return '\n'.join(spins)


if __name__ == '__main__':
    N = read_single_int()
    rings = read_list_int()
    print(calc_spins(rings))