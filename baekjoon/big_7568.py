# Title: 덩치
# Link: https://www.acmicpc.net/problem/7568

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_big(persons):
    orders = []
    for person in persons:
        count = 0
        for p in persons:
            if person[0] < p[0] and person[1] < p[1]:
                count += 1
        orders.append(count+1)

    return " ".join(map(str, orders))


if __name__ == '__main__':
    N = read_single_int()
    persons = []
    for _ in range(N):
        w, h = read_list_int()
        persons.append((w, h))
    print(get_big(persons))
