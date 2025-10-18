class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        last=-10**18
        count=0
        for num in nums:
            lower=num-k
            upper=num+k
            if last<lower:
                last=lower
            else:
                last+=1
            if last<=upper:
                count+=1
            else:
                last-=1
        return count

        