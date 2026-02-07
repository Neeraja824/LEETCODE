class Solution:
    def minimumDeletions(self, s: str) -> int:
        b,dele=0,0
        for i in range(len(s)):
            if s[i]=='b':
                b+=1
            elif b>0:
                b-=1
                dele+=1
        return dele
