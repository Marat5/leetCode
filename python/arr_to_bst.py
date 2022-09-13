# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        rootI = len(nums) // 2
        root = TreeNode(nums[rootI], left=self.sortedArrayToBST(
            nums[:rootI]), right=self.sortedArrayToBST(nums[rootI + 1:]))
        return root


nums = [-10, -3, 0, 5, 9]
s = Solution()
res = s.sortedArrayToBST(nums)
print(res.val, res.left.val, res.right.val)
