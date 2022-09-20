from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Longest common subarray (not subsequence)
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        result = 0
        for i1, n1 in enumerate(nums1):
            for i2, n2 in enumerate(nums2):
                if n1 == n2:
                    dp[i1 + 1][i2 + 1] = dp[i1][i2] + 1
                    result = max(result, dp[i1][i2] + 1)

        return result


nums1 = [0, 1, 1, 1, 1]
nums2 = [1, 0, 1, 0, 1]
print(Solution().findLength(nums1, nums2))
