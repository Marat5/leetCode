import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        n = len(heights)

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            heapq.heappush(min_heap, diff)

            if len(min_heap) > ladders:
                bricks_needed = heapq.heappop(min_heap)
                bricks -= bricks_needed

            if (bricks < 0):
                return i

        return n - 1


res = Solution().furthestBuilding([1, 5, 1, 2, 3, 4, 10000], 4, 1)  # 5
print(res)
