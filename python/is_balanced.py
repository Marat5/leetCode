# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.countHeight(root.right), self.countHeight(root.left)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        lh = self.countHeight(root.left)
        rh = self.countHeight(root.right)
        return abs(lh - rh) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
