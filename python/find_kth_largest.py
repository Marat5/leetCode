from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


res = Solution().findKthLargest([1, 4, 3, 77], 1)
print(res)
