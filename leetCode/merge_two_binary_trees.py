# Title: Merge Two Binary Trees
# Link: https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == root2 == None:
            return None

        root = TreeNode()
        root.val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if  root1 else None, root2.right if root2 else None)

        return root



def solution():
    root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    problem = Problem()
    return problem.mergeTrees(root1, root2)


def main():
    print(solution())


if __name__ == '__main__':
    main()