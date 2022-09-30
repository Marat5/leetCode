from functools import reduce


class Solution:
    # Iterating reversed string
    # def titleToNumber(self, columnTitle: str) -> int:
    #     total = 0
    #     multiplier = 1
    #     for i in range(len(columnTitle) - 1, -1, -1):
    #         c = columnTitle[i]
    #         dec = ord(c) - ord("A") + 1
    #         multiplied = dec * multiplier
    #         total += multiplied
    #         multiplier *= 26

    #     return total

    # Iterating non-reversed string
    # def titleToNumber(self, columnTtile: str) -> int:
    #     total = 0
    #     for c in columnTtile:
    #         total = total * 26 + (ord(c) - ord("A") + 1)
    #     return total

    # One liner
    def titleToNumber(self, columnTitle: str) -> int:
        return reduce(lambda total, c: total * 26 + ord(c) - ord("A") + 1, columnTitle, 0)


print(Solution().titleToNumber("ZY"))
