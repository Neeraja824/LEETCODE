class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        c=dict(Counter(nums))
        for key in c:
            if c[key]==len(nums)//2:
                return key
        