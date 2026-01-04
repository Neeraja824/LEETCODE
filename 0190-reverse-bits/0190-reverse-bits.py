class Solution:
    def reverseBits(self, n: int) -> int:
        nbin=bin(n)[2:].zfill(32)
        def f(i,j):
            if i==j:
                return nbin[i]
            if i>j:
                return ""
            return nbin[j]+f(i+1,j-1)+nbin[i]
        return int(f(0,31),2)