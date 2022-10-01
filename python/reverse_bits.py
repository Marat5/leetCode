class Solution:
    # def reverseBits(self, n: int) -> int:
    #     s = format(n, "32b")
    #     arr = []
    #     for i in s:
    #         if i == "0" or i == " ":
    #             arr.append("0")
    #         else:
    #             arr.append("1")
    #     arr = reversed(arr)
    #     return int("".join(arr), 2)

    # A smarter way to use format
    def reverseBits(self, n: int) -> int:
        return int("{0:032b}".format(n)[::-1], 2)


print(Solution().reverseBits(0b00000010100101000001111010011100))
