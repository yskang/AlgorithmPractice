# Title: Longest Univalue Path
# Link: https://leetcode.com/problems/longest-univalue_path/

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem:
    def longest_univalue_path(self, root: TreeNode) -> int:
        ans = [0]
        self.max_depth(root, ans)
        return ans[0]

    def max_depth(self, root: TreeNode, ans: List) -> int:
        if not root:
            return 0
        
        max_depth_left, max_depth_right = self.max_depth(root.left, ans), self.max_depth(root.right, ans)


        if root.left and root.right:
            if root.left.val == root.right.val == root.val:
                ans[0] = max(ans[0], max_depth_left + max_depth_right+2)
                return max(max_depth_left, max_depth_right) + 1
            if root.left.val == root.val and root.val != root.right.val:
                ans[0] = max(ans[0], max_depth_left+1)
                return max_depth_left + 1
            if root.left.val != root.val and root.val == root.right.val:
                ans[0] = max(ans[0], max_depth_right+1)
                return max_depth_right + 1
        else:
            if root.left and root.val == root.left.val:
                ans[0] = max(ans[0], max_depth_left+1)
                return max_depth_left + 1
            if root.right and root.val == root.right.val:
                ans[0] = max(ans[0], max_depth_right+1)
                return max_depth_right + 1
        return 0


def solution():
    root = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, TreeNode(5)))
    problem = Problem()
    return problem.longest_univalue_path(root)


def main():
    print(solution())


if __name__ == '__main__':
    main()
