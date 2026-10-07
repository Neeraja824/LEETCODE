class Solution:
    def removeInvalidParentheses(self, s: str):
        left = 0
        right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        result = set()
        def dfs(index, left, right, balance, path):
            if index == len(s):
                if left == 0 and right == 0 and balance == 0:
                    result.add("".join(path))
                return
            ch = s[index]
            if ch == '(' and left > 0:
                dfs(index + 1, left - 1, right, balance, path)
            if ch == ')' and right > 0:
                dfs(index + 1, left, right - 1, balance, path)
            if ch == '(':
                path.append(ch)
                dfs(index + 1, left, right, balance + 1, path)
                path.pop()
            elif ch == ')':
                if balance > 0:
                    path.append(ch)
                    dfs(index + 1, left, right, balance - 1, path)
                    path.pop()
            else:
                path.append(ch)
                dfs(index + 1, left, right, balance, path)
                path.pop()
        dfs(0, left, right, 0, [])
        return list(result)