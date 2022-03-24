# Title: DSHS Bank
# Link: https://www.acmicpc.net/problem/16210

import sys
import collections

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, banks: list, xs: list, ys: list):
    x_dic, y_dic = {}, {}

    xs = sorted(xs)
    ys = sorted(ys)
    xs = [0] + xs + [0]
    ys = [0] + ys + [0]
    sum_left_x = 0
    sum_right_x = sum(xs[2:])
    sum_left_y = 0
    sum_right_y = sum(ys[2:])

    for k in range(1, n+1):
        x_dic[xs[k]] = (2*k-n-1)*xs[k] - sum_left_x + sum_right_x
        y_dic[ys[k]] = (2*k-n-1)*ys[k] - sum_left_y + sum_right_y
        sum_left_x += xs[k]
        sum_right_x -= xs[k+1]
        sum_left_y += ys[k]
        sum_right_y -= ys[k+1]

    min_distance = 99999999999999999999
    ans = -1
    for i, (x, y) in enumerate(banks, 1):
        if x_dic[x] + y_dic[y] < min_distance:
            min_distance = x_dic[x] + y_dic[y]
            ans = i

    return ans



def main():
    n = read_single_int()
    banks = []
    xs = []
    ys = []
    for _ in range(n):
        x, y = read_list_int()
        xs.append(x)
        ys.append(y) 
        banks.append((x, y))
    print(solution(n, banks, xs, ys))


if __name__ == '__main__':
    main()