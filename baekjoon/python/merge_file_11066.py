# Title: 파일 합치기
# Link: https://www.acmicpc.net/problem/11066

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_minimum_cost(chapters):
    costs = [[0] * (len(chapters) + 1) for _ in range(len(chapters) + 1)]
    nums = [[0] * (len(chapters) + 1) for _ in range(len(chapters) + 1)]
    sums = [0]

    for c in chapters:
        sums.append(sums[-1]+c)

    for i in range(len(chapters)+1):
        nums[i-1][i] = i+1

    offset = 2
    while offset <= len(chapters):
        start = 0
        while start + offset <= len(chapters):
            if offset == 2:
                costs[start][start+offset] = chapters[start] + chapters[start+1]
            else:
                min_cost = 99999999999
                for n in range(start+1, start+offset):
                    min_cost = min(min_cost, costs[start][n] + costs[n][start+offset])
                costs[start][start+offset] = sum(chapters[start:start+offset]) + min_cost
                costs[start][start+offset] = sums[start+offset]-sums[start] + min_cost
            start += 1
        offset += 1
    return costs[0][len(chapters)]


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        k = read_single_int()
        chapters = read_list_int()
        print(get_minimum_cost(chapters))


