class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        n2=0
        for i in num1:
            digit=ord(i)-ord('0')
            n1=(n1*10)+digit
        for i in num2:
            digit=ord(i)-ord('0')
            n2=(n2*10)+digit
        ans=n1*n2
        return str(ans)
        