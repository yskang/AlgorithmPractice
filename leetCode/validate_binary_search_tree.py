# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        output = []
        self.inorder(root, output)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True

    def inorder(self, root, output):
        if root is None:
            return
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)


if __name__ == "__main__":
    tree0 = TreeNode(0)
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree1.left = tree0
    tree1.right = tree2

    sol = Solution()
    print(sol.isValidBST(tree1))

