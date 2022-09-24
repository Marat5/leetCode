# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val, *self.preorderTraversal(root.left), *self.preorderTraversal(root.right)]


print(Solution().preorderTraversal(TreeNode(0, TreeNode(1), TreeNode(2))))
