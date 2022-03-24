# Title: 트리의 높이와 너비
# Link: https://www.acmicpc.net/problem/2250

import sys

import collections

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


def inorder(node, res, level):
    if node.left:
        inorder(node.left, res, level + 1)
    res.append((node.val, level))
    if node.right:
        inorder(node.right, res, level + 1)


def find_widths(root, N):
    res = []
    widths = collections.defaultdict(lambda: [])
    inorder(root, res, 1)
    for pos, (node, level) in enumerate(res, 1):
        widths[level].append(pos)
    max_levels, max_width = [], 0
    for level in widths.keys():
        width = widths[level][-1] - widths[level][0] + 1
        if max_width < width:
            max_width = width
            max_level = [level]
        elif max_width == width:
            max_level.append(level)
    return '{} {}'.format(min(max_level), max_width)


if __name__ == '__main__':
    N = read_single_int()
    nodes = [None]
    is_root = [True for _ in range(N + 1)]
    for i in range(1, N + 1):
        nodes.append(Node(i))

    for _ in range(N):
        n, l, r = read_list_int()
        if l != -1:
            nodes[n].set_left(nodes[l])
            is_root[l] = False
        if r != -1:
            nodes[n].set_right(nodes[r])
            is_root[r] = False

    root = 1
    for i in range(1, N + 1):
        if is_root[i]:
            root = i
    print(find_widths(nodes[root], N))
