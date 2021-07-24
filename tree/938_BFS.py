# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        queue = [root]
        ans = 0

        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            if node.val < low:
                queue.append(node.right)
            elif node.val > high:
                queue.append(node.left)
            else:
                ans += node.val
                queue.append(node.left)
                queue.append(node.right)

        return ans