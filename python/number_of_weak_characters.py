from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Naive
        # count = 0
        # for p in properties:
        #     for compare_p in properties:
        #         if p[0] < compare_p[0] and p[1] < compare_p[1]:
        #             count += 1
        #             break

        # return count

        # Sorting
        properties.sort(key=lambda x: (-x[0], x[1]))
        count = 0
        current_max = 0
        for _, d in properties:
            if d >= current_max:
                current_max = d
            else:
                count += 1

        return count


s = Solution()
print(s.numberOfWeakCharacters([[2, 2], [3, 3]]))
