# Title: Minimum Distance Between BST Nodes
# Link: https://leetcode.com/problems/minimum-distance-between-bst-nodes/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Problem:
    def __init__(self) -> None:
        self.last = -10**10
        self.min_diff = 10**10

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.min_diff = min(self.min_diff, root.val - self.last)
        self.last = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
        
        return self.min_diff

def solution():
    root = TreeNode()
    problem = Problem()
    return problem.minDiffInBST(root)


def main():
    print(solution())


if __name__ == '__main__':
    main()