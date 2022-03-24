# Title: 지능형 기차
# Link: https://www.acmicpc.net/problem/2455

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_maximum_person(ins, outs):
    train = 0
    max_person = -1
    for i in range(4):
        train -= outs[i]
        train += ins[i]
        max_person = max(max_person, train)
    return max_person


if __name__ == '__main__':
    ins, outs = [], []
    for _ in range(4):
        o, i = read_list_int()
        outs.append(o)
        ins.append(i)
    print(get_maximum_person(ins, outs))