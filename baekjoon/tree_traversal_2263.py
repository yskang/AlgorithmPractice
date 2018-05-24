# Title: 트리의 순회
# Link: https://www.acmicpc.net/problem/2263

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_preorder(inorder_start, postorder_start, length, preorder, inorder_dict, inorder, postorder):
    root = postorder[postorder_start+length-1]
    root_index = inorder_dict[root]

    left_length = root_index - inorder_start
    right_length = length - left_length - 1

    preorder.append(root)

    if left_length == 1:
        preorder.append(postorder[postorder_start])
    elif left_length > 1:
        get_preorder(inorder_start, postorder_start, left_length, preorder, inorder_dict, inorder, postorder)

    if right_length == 1:
        preorder.append(postorder[postorder_start + left_length])
    elif right_length > 1:
        get_preorder(root_index + 1, postorder_start + left_length, right_length, preorder, inorder_dict, inorder, postorder)


if __name__ == '__main__':
    n = read_single_int()
    inorder = read_list_int()
    postorder = read_list_int()
    inorder_dict = {a: i for i, a in enumerate(inorder)}
    preorder = []
    get_preorder(0, 0, len(postorder), preorder, inorder_dict, inorder, postorder)
    print(' '.join(map(str, preorder)))