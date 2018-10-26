# Title: 이진 검색 트리
# Link: https://www.acmicpc.net/problem/5639

import sys

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def pre_order_2_post_order(pre_order: list, start: int, end: int):
    if start >= end:
        return

    if start == 0 and end == 4:
        print('here')

    root = pre_order[start]
    point = start+1

    for i, n in enumerate(pre_order[start+1:end], start+1):
        if n > root:
            point = i
            break

    pre_order_2_post_order(pre_order, start+1, point)
    pre_order_2_post_order(pre_order, point, end)
    print(root)
    return


def solution(pre_order: list):
    pre_order_2_post_order(pre_order, 0, len(pre_order))
    return


def main():
    pre_order = []
    while True:
        try:
            pre_order.append(read_single_int())
        except:
            break
    solution(pre_order)


if __name__ == '__main__':
    main()