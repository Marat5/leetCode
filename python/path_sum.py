# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS, preorder tree traversal
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSumForSubTrees = targetSum - root.val
        if not root.left and not root.right:
            return targetSumForSubTrees == 0

        return self.hasPathSum(root.left, targetSumForSubTrees) or self.hasPathSum(root.right, targetSumForSubTrees)

    # BFS, preorder tree traversal (slower, I made it to practice bfs)
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     queue = [(root, targetSum)]

    #     while queue:
    #         current_node, target = queue.pop(0)
    #         if not current_node:
    #             continue

    #         if not current_node.left and not current_node.right and target == current_node.val:
    #             return True

    #         queue.append((current_node.left, target - current_node.val))
    #         queue.append((current_node.right, target - current_node.val))

    #     return False


print(Solution().hasPathSum(TreeNode(12, TreeNode(
    2, TreeNode(11), TreeNode(12)), TreeNode(3, TreeNode(1), TreeNode(2))), 16))
