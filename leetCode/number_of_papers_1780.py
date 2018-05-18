# Title: 종이의 개수
# Link: https://www.acmicpc.net/problem/1780

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def check_all_number(matrix, start_x, start_y, length):
    base = matrix[start_y][start_x]

    if length == 1:
        return base

    for y in range(start_y, start_y+length):
        for x in range(start_x, start_x+length):
            if matrix[y][x] != base:
                return 9

    return base


def number_of_papers(matrix, start_x, start_y, length):
    index = [-1, 0, 1]
    sums = {-1: 0, 0: 0, 1: 0}

    base = matrix[start_y][start_x]

    if length != 1:
        done = False
        for y in range(start_y, start_y+length):
            for x in range(start_x, start_x+length):
                if matrix[y][x] != base:
                    base = 9
                    done = True
                    break
            if done:
                break

    if base != 9:
        sums[base] += 1
    else:
        new_length = length // 3

        for x in range(3):
            for y in range(3):
                s = number_of_papers(matrix, start_x + new_length * x, start_y + new_length * y, new_length)
                for i in index:
                    sums[i] += s[i]
    return sums


if __name__ == '__main__':
    N = read_single_int()
    matrix = []
    for _ in range(N):
        matrix.append(read_list_int())
    ret = number_of_papers(matrix, 0, 0, N)
    for i in ret:
        print(ret[i])