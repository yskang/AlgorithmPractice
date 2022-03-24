# Title: 히스토그램에서 가장 큰 직사각형
# Link: https://www.acmicpc.net/problem/6549

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def init_segment_min(array, tree, node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    mid = (start + end) // 2
    left = init_segment_min(array, tree, node * 2, start, mid)
    right = init_segment_min(array, tree, node * 2 + 1, mid + 1, end)
    if array[left] < array[right]:
        tree[node] = left
    else:
        tree[node] = right
    return tree[node]


def find_min(array, tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    left_index = find_min(array, tree, node*2, start, (start+end)//2, left, right)
    right_index = find_min(array, tree, node*2+1, (start+end)//2+1, end, left, right)
    if left_index == -1 and right_index == -1:
        return -1
    elif left_index == -1:
        return right_index
    elif right_index == -1:
        return left_index
    else:
        if array[left_index] < array[right_index]:
            return left_index
        return right_index


def get_biggest_square(heights, tree, start, end):
    n = len(heights)
    m = find_min(heights, tree, 1, 0, n-1, start, end)
    area = (end-start+1)*heights[m]

    if start <= m-1:
        temp = get_biggest_square(heights, tree, start, m-1)
        if area < temp:
            area = temp
    if m+1 <= end:
        temp = get_biggest_square(heights, tree, m+1, end)
        if area < temp:
            area = temp
    return area


if __name__ == '__main__':
    while True:
        histogram = read_list_int()
        if histogram == [0]:
            break
        histogram = histogram[1:]
        tree = [0 for _ in range(len(histogram)*4)]
        segment_tree = init_segment_min(histogram, tree, 1, 0, len(histogram)-1)
        print(get_biggest_square(histogram, tree, 0, len(histogram)-1))
