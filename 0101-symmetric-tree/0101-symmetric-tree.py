# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(n1,n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val!=n2.val:
                return False
            return check(n1.right,n2.left) and check(n2.right,n1.left)
        return check(root.left,root.right)