class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=[val for val in s if val.isalnum()]
        z="".join(y)
        z=z.lower()
        if z==z[::-1]:
            return True
        else:
            return False
        