# Title: Range Sum of BST
# Link: https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem:
    def __init__(self) -> None:
        self.acc = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if low <= root.val <= high:
            self.acc += root.val
        if root.left and low < root.val:
            self.rangeSumBST(root.left, low, high)
        if root.right and root.val < high:
            self.rangeSumBST(root.right, low, high)
        return self.acc


def solution():
    root = TreeNode()
    problem = Problem()
    return problem.rangeSumBST(root, 7, 15)


def main():
    print(solution())


if __name__ == '__main__':
    main()