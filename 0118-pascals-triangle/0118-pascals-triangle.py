class Solution:
    def generate(self, n: int) -> List[List[int]]:
        dp=[[1]]
        if n==1:
            return dp
        dp.append([1,1])
        if n==2:
            return dp
        for i in range(2,n):
            dpi=[1]
            for j in range(len(dp[i-1])-1):
                dpi.append(dp[i-1][j]+dp[i-1][j+1])
            dpi.append(1)
            dp.append(dpi)
        return dp
        