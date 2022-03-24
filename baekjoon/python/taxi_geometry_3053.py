# Title: 택시 기하학
# Link: https://www.acmicpc.net/problem/3053
import math
import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def area_euclid(r):
    return math.pi * r * r


def area_taxi(r):
    return r * r * 2


if __name__ == '__main__':
    r = read_single_int()
    print("{0:.6f}".format(area_euclid(r)))
    print("{0:.6f}".format(area_taxi(r)))