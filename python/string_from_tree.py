# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""

        if not root:
            return res

        res += str(root.val)

        if root.right != None or root.left != None:
            res += f"({self.tree2str(root.left)})"

        if root.right != None:
            res += f"({self.tree2str(root.right)})"

        return res


root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
s = Solution()

print(s.tree2str(root))
