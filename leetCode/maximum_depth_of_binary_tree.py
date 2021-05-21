# Title: Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem:
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


def solution():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    problem = Problem()
    return problem.max_depth(root)


def main():
    print(solution())


if __name__ == '__main__':
    main()