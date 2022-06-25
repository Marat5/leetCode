from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        problem = None
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if problem:
                    return False
                problem = i,

        if not problem:
            return True

        i = problem[0]
        if i == 0 or i == len(nums) - 2 or nums[i - 1] <= nums[i + 1] or nums[i] <= nums[i + 2]:
            return True

        return False


res = Solution().checkPossibility([1, 4, 1, 2])
print(res)
