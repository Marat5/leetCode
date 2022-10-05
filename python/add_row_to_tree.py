# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        queue = [(root, 1)]
        while queue:
            cur, cur_depth = queue.pop(0)
            if not cur:
                continue

            if cur_depth < depth - 1:
                queue.append((cur.left, cur_depth + 1))
                queue.append((cur.right, cur_depth + 1))
            elif cur_depth == depth - 1:
                cur.left = TreeNode(val, left=cur.left)
                cur.right = TreeNode(val, right=cur.right)

        return root
