class Solution:
    def get_longest(self, s: str, l: int, r: int):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            longest_for_i_center_odd = self.get_longest(s, i, i)
            longest_for_i_center_even = self.get_longest(s, i, i + 1)
            longest_for_i_center = longest_for_i_center_even if len(longest_for_i_center_even) > len(
                longest_for_i_center_odd) else longest_for_i_center_odd

            if len(longest_for_i_center) > len(longest):
                longest = longest_for_i_center

        return longest


s = Solution()
print(s.longestPalindrome("cbbd"))
