# Title: Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root) -> str:
        if not root:
            return '[]'
        ans = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append('null')

        i = -1
        while True:
            if ans[i] != 'null':
                break
            i -= 1

        return f"[{','.join(ans[:len(ans)+i+1])}]"

    def deserialize(self, data) -> TreeNode:
        if data == '[]':
            return None

        data = data[1:-1].split(',')
        data = list(reversed(data))
        rows = deque()
        next_rows = deque()

        v = data.pop()
        root = TreeNode(v)
        rows.append(root)

        while data:
            while rows:
                node = rows.popleft()
                left_val = data.pop() if data else 'null'
                right_val = data.pop() if data else 'null'
                if left_val != 'null':
                    node.left = TreeNode(left_val)
                    next_rows.append(node.left)
                if right_val != 'null':
                    node.right = TreeNode(right_val)
                    next_rows.append(node.right)
            rows, next_rows = next_rows, deque()

        return root


class Problem:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return (abs(self.max_depth(root.left) - self.max_depth(root.right)) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

def solution():
    codec = Codec()
    root = codec.deserialize('[1,2,2,3,3,null,null,4,4]')
    problem = Problem()
    return problem.isBalanced(root)


def main():
    print(solution())


if __name__ == '__main__':
    main()