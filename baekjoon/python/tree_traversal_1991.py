# Title: 트리 순회
# Link: https://www.acmicpc.net/problem/1991

import sys
import string

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_list_str():
    return sys.stdin.readline().strip().split(' ')


def read_single_int():
    return int(sys.stdin.readline().strip())


class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


def preorder(node, res):
    res.append(node.name)
    if node.left:
        preorder(node.left, res)
    if node.right:
        preorder(node.right, res)


def inorder(node, res):
    if node.left:
        inorder(node.left, res)
    res.append(node.name)
    if node.right:
        inorder(node.right, res)


def post(node, res):
    if node.left:
        post(node.left, res)
    if node.right:
        post(node.right, res)
    res.append(node.name)


def traversal_preorder(node):
    res = []
    preorder(node, res)
    return ''.join(res)


def traversal_inorder(node):
    res = []
    inorder(node, res)
    return ''.join(res)


def traversal_postorder(node):
    res = []
    post(node, res)
    return ''.join(res)


if __name__ == '__main__':
    N = read_single_int()
    nodes = {'.': None}
    for n in range(N):
        nodes[string.ascii_uppercase[n]] = Node(string.ascii_uppercase[n])
    for _ in range(N):
        node, left, right = read_list_str()
        nodes[node].set_left(nodes[left])
        nodes[node].set_right(nodes[right])

    print(traversal_preorder(nodes['A']))
    print(traversal_inorder(nodes['A']))
    print(traversal_postorder(nodes['A']))