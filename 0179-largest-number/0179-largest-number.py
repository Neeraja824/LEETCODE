class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s=[str(num) for num in nums]
        from functools import cmp_to_key
        s.sort(key=cmp_to_key(lambda a,b: -1 if a+b > b+a else 1))
        if s[0]=="0":
            return "0"
        ans="".join(s)
        return ans
        