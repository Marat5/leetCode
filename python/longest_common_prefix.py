from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0

        while True:
            # Iteration through char indexes
            if len(strs[0]) <= i:
                break

            char = strs[0][i]
            is_char_everywhere = True

            for str in strs:
                # Iteration through all strings to check for current index
                if len(str) <= i or str[i] != char:
                    is_char_everywhere = False
                    break

            if is_char_everywhere:
                res += char
                i += 1
            else:
                break

        return res


res = Solution().longestCommonPrefix(["flee", "flow", "flight"])
print(res)
