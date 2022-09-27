class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            res.append(chr(65 + rem))
            columnNumber = columnNumber // 26

        return "".join(list(reversed(res)))


print(Solution().convertToTitle(27))
