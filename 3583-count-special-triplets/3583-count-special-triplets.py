class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        total=Counter(nums)
        left=Counter()
        cnt=0
        mod=10**9+7
        for n in nums:
            tar=n*2
            total[n]-=1
            l=left.get(tar,0)
            r=total.get(tar,0)
            if l>=1 and r>=1:
                cnt=(cnt+l*r)%mod
            left[n]+=1
        return cnt
