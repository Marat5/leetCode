# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSumForSubTrees = targetSum - root.val
        if not root.left and not root.right:
            return targetSumForSubTrees == 0

        return self.hasPathSum(root.left, targetSumForSubTrees) or self.hasPathSum(root.right, targetSumForSubTrees)
