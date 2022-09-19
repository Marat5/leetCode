from typing import List


class Solution:
    # dp solution
    # def getRow(self, rowIndex: int) -> List[int]:
    #     row = [1] * (rowIndex + 1)
    #     for i in range(2, rowIndex + 1):
    #         for j in range(1, i):
    #             row[i-j] += row[i-j-1]
    #     return row

    # math formula solution
    def getRow(self, r) -> List[int]:
        ans = [1]*(r+1)
        up = r
        down = 1
        for i in range(1, r):
            ans[i] = ans[i-1]*up//down
            up = up - 1
            down = down + 1
        return ans


print(Solution().getRow(4))
