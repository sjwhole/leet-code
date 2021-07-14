from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        queue = deque([root])
        result = ["#"]

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append("#")
        return " ".join(result)

    def deserialize(self, data):
        if data == "# #":
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = deque([root])
        idx = 2
        while queue:
            node = queue.popleft()
            if nodes[idx] != "#":
                node.left = TreeNode(int(nodes[idx]))
                queue.append(node.left)
            idx += 1

            if nodes[idx] != "#":
                node.right = TreeNode(int(nodes[idx]))
                queue.append(node.right)
            idx += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
