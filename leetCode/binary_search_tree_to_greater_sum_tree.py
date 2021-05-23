# Title: Binary Search Tree to Greater Sum Tree
# Link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Problem:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodes = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            nodes.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        nodes = sorted(nodes)
        s = sum(nodes)
        new_nodes = defaultdict(lambda: -1)

        for node in nodes:
            new_nodes[node] = s-node
            s -= node

        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            node.val = new_nodes[node.val]

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)        


        return root

def solution():
    root = TreeNode()
    problem = Problem()
    return problem.bstToGst(root)


def main():
    print(solution())


if __name__ == '__main__':
    main()