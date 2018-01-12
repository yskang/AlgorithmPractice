import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, node, route, targetA, targetB):
        if node is None:
            return

        route.append(node.val)

        self.dfs(node.left, route, targetA, targetB)
        self.dfs(node.right, route)

    def lowestCommonAncestor(self, root, p, q):
        p.left = None
        p.right = None
        q.left = None
        q.right = None

        route = []

        self.dfs(root, route, p.val, q.val)


        return None


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


class Example_Test(unittest.TestCase):
    def test_sol_1(self):
        self.assertEqual(sol.lowestCommonAncestor(root, node_5, node_1), node_3, msg="Wrong!")
    def test_sol_2(self):
        self.assertEqual(sol.lowestCommonAncestor(root, node_5, node_4), node_5, msg="Wrong!")



if __name__ == '__main__':
    unittest.main()
