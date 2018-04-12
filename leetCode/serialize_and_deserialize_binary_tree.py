# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        if root is None:
            return "[]"
        serialized = []
        queue = []
        current = root

        while True:
            if current is not None:
                serialized.append(str(current.val))
                queue.append(current.left)
                queue.append(current.right)
            else:
                serialized.append("null")

            if len(queue) == 0:
                break

            current = queue.pop(0)

        while serialized[-1] == "null":
            serialized.pop()

        return "[{}]".format(",".join(serialized))

    def deserialize(self, data):
        if data == "[]":
            return None
        ds = data.replace("[", "").replace("]", "").split(",")
        queue = []
        root = TreeNode(ds.pop(0))
        queue.append((root, "left"))
        queue.append((root, "right"))

        while len(ds) != 0:
            d = ds.pop(0)
            if d != "null":
                n = TreeNode(d)
                queue.append((n, "left"))
                queue.append((n, "right"))
                t = queue.pop(0)
                if t[1] == "left":
                    t[0].left = n
                else:
                    t[0].right = n

            else:
                queue.pop(0)

        return root


if __name__ == "__main__":
    tree_1 = TreeNode(1)
    tree_2 = TreeNode(2)
    tree_3 = TreeNode(3)
    tree_4 = TreeNode(4)
    tree_5 = TreeNode(5)
    tree_6 = TreeNode(6)

    tree_3.left = tree_4
    tree_3.right = tree_5
    tree_1.left = tree_2
    tree_1.right = tree_3

    codec = Codec()

    print(codec.serialize(tree_1))


