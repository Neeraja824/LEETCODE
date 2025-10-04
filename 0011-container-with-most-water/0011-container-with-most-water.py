class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        n=len(height)
        low,high=0,n-1
        while low < high:
            res=max(res,(high-low)*min(height[low],height[high]))
            if height[high]<=height[low]:
                high-=1
            else:
                low+=1
        return res
        