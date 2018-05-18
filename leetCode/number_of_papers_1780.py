# Title: 종이의 개수
# Link: https://www.acmicpc.net/problem/1780

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def check_all_number(matrix):
    base = matrix[0][0]
    for row in matrix:
        for e in row:
            if e != base:
                return 9
    return base


def separate(matrix):
    parts = [[] for _ in range(9)]
    l = len(matrix) // 3
    for i in range(3):
        for row in matrix[l*i:l*(i+1)]:
            parts[i*3].append(row[0:l])
            parts[i*3+1].append(row[l:2 * l])
            parts[i*3+2].append(row[2 * l:3 * l])
    return parts


def number_of_papers(matrix):
    index = [-1, 0, 1]
    sums = {-1: 0, 0: 0, 1: 0}
    ret = check_all_number(matrix)
    if ret != 9:
        sums[ret] += 1
    else:
        papers = separate(matrix)
        for paper in papers:
            s = number_of_papers(paper)
            for i in index:
                sums[i] += s[i]
    return sums


if __name__ == '__main__':
    N = read_single_int()
    matrix = []
    for _ in range(N):
        matrix.append(read_list_int())
    ret = number_of_papers(matrix)
    for i in ret:
        print(ret[i])