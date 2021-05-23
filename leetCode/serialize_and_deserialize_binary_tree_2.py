# Title: Serialize and Deserialize Binary Tree
# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

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
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

def solution():
    des = Codec()
    des.deserialize('[1,2]')


def main():
    print(solution())


if __name__ == '__main__':
    main()