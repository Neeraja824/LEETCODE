class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for ch in s:
            if ch=="(":
                stack.append(0)
            else:
                x=stack.pop()
                score=1 if x==0 else 2*x
                stack[-1]+=score
        return stack[0]
