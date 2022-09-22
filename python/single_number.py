

from functools import reduce
from typing import List


class Solution:
    # No bitwise, but spends space (O(n) space at most)
    # def singleNumber(self, nums: List[int]) -> int:
    #     ans = {}
    #     for n in nums:
    #         if n in ans:
    #             del ans[n]
    #         else:
    #             ans[n] = True

    #     return list(ans.keys())[0]

    # Bitwise xor solution
    # def singleNumber(self, nums):
    #     res = 0
    #     for num in nums:
    #         res ^= num
    #     return res

    # Bitwise xor solution with reduce
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


print(Solution().singleNumber([2, 2, 1]))
