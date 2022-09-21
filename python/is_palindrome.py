

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Stack solution
        s = s.lower()
        alpha_numeric_stack = []
        for c in s:
            c.lower()
            if c.isalnum():
                alpha_numeric_stack.append(c)

        for c in s:
            if c.isalnum() and c != alpha_numeric_stack.pop():
                return False

        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
