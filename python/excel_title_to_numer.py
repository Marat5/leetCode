class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        multiplier = 1
        for i in range(len(columnTitle) - 1, -1, -1):
            c = columnTitle[i]
            dec = ord(c) - ord("A") + 1
            multiplied = dec * multiplier
            total += multiplied
            multiplier *= 26

        return total


print(Solution().titleToNumber("ZY"))
