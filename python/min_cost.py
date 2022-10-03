from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        i = 0
        while i < len(colors):
            max_candidate_value = 0
            first_color_in_sequence = colors[i]
            while i < len(colors) and first_color_in_sequence == colors[i]:
                total += neededTime[i]
                max_candidate_value = max(neededTime[i], max_candidate_value)
                i += 1

            total -= max_candidate_value
        return total


print(Solution().minCost("abaac", [1, 2, 3, 4, 5]))
