

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Stack solution
        # s = s.lower()
        # alpha_numeric_stack = []
        # for c in s:
        #     c.lower()
        #     if c.isalnum():
        #         alpha_numeric_stack.append(c)

        # for c in s:
        #     if c.isalnum() and c != alpha_numeric_stack.pop():
        #         return False

        # return True

        # Two pointers solution
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


print(Solution().isPalindrome(".,"))
