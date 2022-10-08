from typing import List


class Solution:
    # Too slow
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     nums.sort()
    #     closest_sum = float("inf")
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             for k in range(j + 1, len(nums)):
    #                 is_closer = abs(
    #                     target - (nums[i] + nums[j] + nums[k])) < abs(target - closest_sum)
    #                 if is_closer:
    #                     closest_sum = nums[i] + nums[j] + nums[k]

    #     return closest_sum

    # Also gets time limit
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     nums.sort()
    #     res = sum(nums[:3])
    #     for i in range(len(nums)):
    #         l = i + 1
    #         r = len(nums) - 1
    #         while l < r:
    #             s = sum((nums[i], nums[l], nums[r]))
    #             if abs(target-s) < abs(target-res):
    #                 res = s

    #             if s > target:
    #                 r -= 1
    #             elif s < target:
    #                 l += 1
    #             else:
    #                 return res
    #     return res

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current

        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key=lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i > 0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
