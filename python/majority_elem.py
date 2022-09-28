from typing import List


class Solution:
    # Regular solution
    # def majorityElement(self, nums: List[int]) -> int:
    #     target_count = len(nums) // 2
    #     hm = defaultdict(lambda: 0)
    #     for n in nums:
    #         hm[n] += 1
    #         if hm[n] > target_count:
    #             return n

    # Constant space solution Boyer-Moore majority vote algorigthm
    def majorityElement(self, nums: List[int]) -> int:
        currentMajor = None
        count = 0
        for elem in nums:
            if count == 0:
                count += 1
                currentMajor = elem
            elif currentMajor == elem:
                count += 1
            else:
                count -= 1

        return currentMajor


print(Solution().majorityElement([3, 2, 3]))
