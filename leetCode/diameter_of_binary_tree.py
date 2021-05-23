# Title: Diameter of Binary Tree
# Link: https://leetcode.com/problems/diameter-of-binary-tree/

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        ans = [0]
        self.max_depth(root, ans)
        return ans[0]

    def max_depth(self, root: TreeNode, ans: List) -> int:
        if not root:
            return 0
        max_left = self.max_depth(root.left, ans)
        max_right = self.max_depth(root.right, ans)
        ans[0] = max(max_left + max_right, ans[0])
        return max(max_left, max_right) + 1


def solution():
    root = TreeNode(0)
    problem = Problem()
    return problem.diameter_of_binary_tree(root)


def main():
    print(solution())


if __name__ == '__main__':
    main()