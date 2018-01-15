import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.found = 0
        self.paths = []
        self.route = []

    def dfs(self, node, targetA, targetB):
        if node is targetA or node is targetB:
            self.found += 1
            temp = self.route[:]
            temp.append(node)
            self.paths.append(temp)

        if self.found is 2:
            return

        self.route.append(node)

        if node.left:
            self.dfs(node.left, targetA, targetB)
        if node.right:
            self.dfs(node.right, targetA, targetB)

        self.route.pop()

    def lowestCommonAncestor(self, root, p, q):
        self.found = 0
        self.dfs(root, p, q)

        i = 0
        while True:
            if len(self.paths[0]) <= i or len(self.paths[1]) <= i:
                return self.paths[0][i-1]
            elif self.paths[0][i] != self.paths[1][i]:
                return self.paths[0][i-1]
            else:
                i += 1
                continue

node_1 = TreeNode(1)
node_0 = TreeNode(0)
node_8 = TreeNode(8)
node_7 = TreeNode(7)
node_4 = TreeNode(4)
node_3 = TreeNode(3)
node_5 = TreeNode(5)
node_2 = TreeNode(2)
node_6 = TreeNode(6)

node_1.left = node_0
node_1.right = node_8

node_2.left = node_7
node_2.right = node_4

node_5.left = node_6
node_5.right = node_2

root = node_3
root.left = node_5
root.right = node_1

sol = Solution()

print(sol.lowestCommonAncestor(root, node_5, node_1).val)

node_1 = TreeNode(1)
node_0 = TreeNode(0)
node_8 = TreeNode(8)
node_7 = TreeNode(7)
node_4 = TreeNode(4)
node_3 = TreeNode(3)
node_5 = TreeNode(5)
node_2 = TreeNode(2)
node_6 = TreeNode(6)

node_1.left = node_0
node_1.right = node_8

node_2.left = node_7
node_2.right = node_4

node_5.left = node_6
node_5.right = node_2

root = node_3
root.left = node_5
root.right = node_1

sol = Solution()

print(sol.lowestCommonAncestor(root, node_3, node_1).val)


# class Example_Test(unittest.TestCase):
#     def test_sol_1(self):
#         self.assertEqual(sol.lowestCommonAncestor(root, node_5, node_1), node_3, msg="Wrong!")
#
#     def test_sol_2(self):
#         self.assertEqual(sol.lowestCommonAncestor(root, node_5, node_4), node_5, msg="Wrong!")
#
#
# if __name__ == '__main__':
#     unittest.main()
