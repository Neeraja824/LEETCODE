class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans,pos=0,0
        for letter in reversed(columnTitle):
            d=ord(letter)-64
            ans+=d*26**pos
            pos+=1
        return ans