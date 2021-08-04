# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return

        idx = inorder.index(preorder.pop(0))

        node = TreeNode(inorder[idx])
        node.left = self.buildTree(preorder, inorder[:idx])
        node.right = self.buildTree(preorder, inorder[idx + 1:])

        return node
