# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #     stack = [(root.left, root.right)]
    #     while stack:
    #         l, r = stack.pop()
    #         if not l and not r:
    #             continue
    #         if not l or not r or l.val != r.val:
    #             return False
    #         stack.append((l.left, r.right))
    #         stack.append((l.right, r.left))
    #     return True

    # recursive
    def dfs(self, l, r):
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.dfs(root.left, root.right)


s = Solution()
tree = TreeNode(1, left=TreeNode(2, left=TreeNode(2), right=None),
                right=TreeNode(2, left=TreeNode(2)))
print(s.isSymmetric(tree))
