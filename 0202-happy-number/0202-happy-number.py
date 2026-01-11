class Solution:
    def isHappy(self, n: int) -> bool:
        s=lambda x: x ** 2
        c=n
        while c!=1 and c!=4:
            di=[int(i) for i in str(c)]
            c=sum(s(d) for d in di)
        return c==1