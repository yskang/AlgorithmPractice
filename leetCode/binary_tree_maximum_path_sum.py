class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_value = 0

    def maxPathSum(self, root):
        self.max_value = -999999999999
        self.max_path_down(root)
        return self.max_value

    def max_path_down(self, node):
        if node is None:
            return 0
        left = max(0, self.max_path_down(node.left))
        right = max(0, self.max_path_down(node.right))
        self.max_value = max(self.max_value, left + right + node.val)
        return max(left, right) + node.val


if __name__ == '__main__':
    n_1 = TreeNode(1)
    n_2 = TreeNode(2)
    n_3 = TreeNode(3)

    n_1.left = n_2
    n_1.right = n_3

    sol = Solution()
    print(sol.maxPathSum(n_1))